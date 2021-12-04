.. UserProfile Database documentation master file, created by
   sphinx-quickstart on Sun Nov 21 12:45:31 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to UserProfile Database's documentation!
================================================


.. toctree::
   :maxdepth: 2
   :caption: Read Me:

   README

UserProfile - Main Module
=========================

.. automodule:: main
   :members:
   :undoc-members:

Models - Authenticator
======================

.. automodule:: models.authenticator
   :members:
   :undoc-members:

Models - Classes
================

.. autoclass:: models.classes.CreateLogin(tortoise.models.Model)
   :members:
   :undoc-members:

.. autoclass:: models.classes.Login(tortoise.models.Model)
   :members:
   :undoc-members:

Models - Custom Logging
=======================

.. autoclass:: models.config.LogConfig(pydantic.BaseModel)
   :members:
   :undoc-members:

Models - User Models
====================

.. autoclass:: models.user_models.CustomModels(tortoise.models.Model)
   :members:
   :undoc-members:
   :exclude-members: User_Model, User_i_Model


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
