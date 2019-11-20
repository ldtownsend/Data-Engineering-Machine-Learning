"""Entry point for web API."""
from .app import create_app

#APP is a global variable
APP = create_app()
