from passlib.hash import bcrypt
from tortoise import fields
from tortoise.models import Model


class Login(Model):
    """Creates a datastructure with keys, id, username and password_hash

    >>> Login

    """
    username = fields.CharField(50, unique=True)
    password_hash = fields.CharField(128)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)


class CreateLogin(Model):
    """Creates a datastructure with keys, id, username and password

    >>> CreateLogin

    """
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password = fields.CharField(128)
