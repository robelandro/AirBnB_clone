#!/usr/bin/python3
""" AirBnb project - BaseModel class """

import uuid
from datetime import datetime
import models
import copy


class BaseModel:
    """ This class defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ method constructor """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            form = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                    continue
                if key == "created_at":
                    self.created_at = datetime.strptime(value, form)
                    continue
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, form)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ print a readable string """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary with all keys/value
        of __dict__ of the instance """
        dictnew = copy.deepcopy(self.__dict__)
        dictnew['__class__'] = self.__class__.__name__
        formato = "%Y-%m-%dT%H:%M:%S.%f"
        dictnew['created_at'] = self.created_at.strftime(formato)
        dictnew['updated_at'] = self.updated_at.strftime(formato)
        dictnew['id'] = self.id
        return dictnew
