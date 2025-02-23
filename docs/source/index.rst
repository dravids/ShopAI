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
   api/core
   api/routes
   api/services
   api/models

Project Overview
---------------
ShopAI is a modern API built with FastAPI that \
powers the world's first Shopping AI assistant \
optimized for shopping, featuring location-based \
services and intelligent product recommendations.

API Documentation
------------------
.. autosummary::
   :toctree: _autosummary
   :recursive:

   src.main
   src.core.config
   src.core.exceptions
   src.core.middleware
   src.routes.v1
   src.routes.v1.base_router
   src.routes.v1.health.health_router
   src.routes.v1.location.location_router
   src.services.base_llm_provider
   src.services.location_service
   src.models.user
   src.models.location

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
