# UserProfile Database
A database created using FastAPI to create and maintain UserProfiles.

### Optional Env Variables
- `port` - Port number on which the application should run. Defaults to WW2 start year.
- `JWT_SECRET` - A secret for encoding and decoding. Defaults to url safe UUID.

### Coding Standards
Docstring format: [`Google`](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) <br>
Styling conventions: [`PEP 8`](https://www.python.org/dev/peps/pep-0008/) <br>
Clean code with pre-commit hooks: [`flake8`](https://flake8.pycqa.org/en/latest/) and 
[`isort`](https://pycqa.github.io/isort/)

### Linting
`PreCommit` will ensure linting, and the doc creation are run on every commit.

**Requirement**
<br>
`pip install --no-cache --upgrade sphinx pre-commit recommonmark`

**Usage**
<br>
`pre-commit run --all-files`

### Runbook
[![made-with-sphinx-doc](https://img.shields.io/badge/Code%20Docs-Sphinx-1f425f.svg)](https://www.sphinx-doc.org/en/master/man/sphinx-autogen.html)

[https://thevickypedia.github.io/user_profile_database/](https://thevickypedia.github.io/user_profile_database/)

## License & copyright
&copy; Vignesh Sivanandha Rao

Licensed under the [MIT License](https://github.com/thevickypedia/Jarvis/blob/master/LICENSE)
