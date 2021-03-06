from logging import getLogger
from logging.config import dictConfig
from os import environ
from pathlib import PurePath
from socket import gethostbyname

import jwt
import uvicorn
from fastapi import Depends, FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import PydanticModel

from models.authenticator import (JWT_SECRET, authenticate_user,
                                  get_current_user)
from models.classes import Login
from models.user_models import CustomModels

MODULE = PurePath(__file__).stem  # Name of this file
DATABASE = "UserProfiles"
LOGGER = getLogger(MODULE)
environ['module'] = MODULE
custom_models = CustomModels

app = FastAPI(
    title="UserAccounts",
    description="### API to create and authenticate user profiles.",
    version="v1.0"
)


@app.on_event(event_type='startup')
async def startup_event() -> None:
    """Runs during startup. Configures custom logging using LogConfig."""
    from models.config import LogConfig
    dictConfig(config=LogConfig().dict())


@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def redirect_index() -> str:
    """Redirect to documents.

    Returns:
        str:
        Redirects `/` url to `/docs`
    """
    return '/docs'


@app.get('/status', include_in_schema=False)
def health() -> dict:
    """Health Check for FileFeeder.

    Returns:
        dict:
        Health status in a dictionary.
    """
    return {'Message': 'Healthy'}


@app.post('/generate-token')  # Endpoint should match with the tokenUrl of oauth2_scheme in authenticator.py
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()) -> dict:
    """Generates a jwt for the credentials received.

    Args:
        form_data: Takes the ``OAuth2PasswordRequestForm`` model as an argument.

    Returns:
        dict:
        Returns a dictionary of ``access_token`` and ``token_type``

    See Also:

        - This function is enabled only for test purpose.

        - The actual working of the working is done using the endpoint ``generate-token``

        - It is passed as ``tokenUrl`` to the ``fastapi`` class ``OAuth2PasswordBearer`` which is our ``oauth2_scheme``
    """
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail=status.HTTP_401_UNAUTHORIZED)
    user_obj = await custom_models.User_Model.from_tortoise_orm(obj=user)
    token = jwt.encode(payload=user_obj.dict(), key=JWT_SECRET, algorithm='HS256')
    return {'access_token': token, 'token_type': 'bearer'}


@app.post('/create-user', response_model=custom_models.User_Model)
async def create_user(user: custom_models.User_i_Model) -> PydanticModel:
    """Creates a new user profile and stores it in the database.

    Args:
        user: Takes the internal user profile model as an argument.

    Returns:
        PydanticModel:
        Returns a PyDantic model.
    """
    user_obj = Login(username=user.username, password_hash=bcrypt.hash(user.password))
    await user_obj.save()
    LOGGER.info(f'sqlite3 db.{DATABASE}')
    LOGGER.info('SELECT * FROM login;')
    return await custom_models.User_Model.from_tortoise_orm(obj=user_obj)


@app.get('/authenticate', response_model=custom_models.User_Model)
async def authenticate(user: custom_models.User_Model = Depends(get_current_user)) -> PydanticModel:
    """Authenticates any user per the information stored in the database.

    Args:
        user: Takes the User_Pydantic model as an argument.

    Returns:
        PydanticModel:
        Returns the user profile information.

    See Also:
        This is just a placeholder, and a method for further development.
    """
    return user


register_tortoise(
    app=app,
    db_url=f'sqlite://db.{DATABASE}',
    modules={
        'models': [MODULE]
    },
    generate_schemas=True,
    add_exception_handlers=True
)


if __name__ == '__main__':
    argument_dict = {
        "app": f"{MODULE or __name__}:app",
        "host": gethostbyname('localhost'),
        "port": int(environ.get('port', 1939)),
        "reload": True
    }
    uvicorn.run(**argument_dict)
