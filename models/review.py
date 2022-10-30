#!/usr/bin/python3
"""user class that inherits from BaseModels
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review Class
    """
    place_id = ""
    user_id = ""
    text = ""