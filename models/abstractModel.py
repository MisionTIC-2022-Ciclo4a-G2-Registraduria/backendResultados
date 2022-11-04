from abc import ABCMeta

class AbstractModel(metaclass=ABCMeta):

    def __init__(self, data: dict):
        """
        This constructor is used to transform a dictionary called data
        into an object making a flexible attribute definition
        :param data:
        """
        for key, value in data.items():
            setattr(self, key, value)
