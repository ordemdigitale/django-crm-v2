# import celery
"""
import the celery module in the __init__.py file of the project
to make sure it is loaded when Django starts.
"""
from .celery import app as celery_app

__all__ = ('celery_app',)