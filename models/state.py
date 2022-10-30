#!/usr/bin/python3
"""State class that inherits from BaseModels
"""

from unicodedata import name
from models.base_model import BaseModel


class State(BaseModel):
    """ The state class"""
    name = ""
