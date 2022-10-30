#!/usr/bin/python3
"""user class that inherits from BaseModels
"""

from models.base_model import BaseModel


class User(BaseModel):
    """The class used to retrive basic user information"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
