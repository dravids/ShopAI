.. ShopAI documentation master file, created by
   sphinx-quickstart on Thu Feb  6 05:41:20 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ShopAI Documentation
===================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api/modules
   api/main
   api/services
   api/models

Project Overview
--------------
ShopAI is a modern API built with FastAPI that \
powers the world's first Shopping AI assistant \
optimized for shopping

API Documentation
---------------
.. autosummary::
   :toctree: _autosummary
   :recursive:

   src.main
   src.services.base_llm_provider
   src.models.user

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`