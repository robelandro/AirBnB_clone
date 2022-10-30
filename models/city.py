#!/usr/bin/python3
"""City class that inherits from BaseModels
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ The City class"""
    state_id = ""
    name = ""
