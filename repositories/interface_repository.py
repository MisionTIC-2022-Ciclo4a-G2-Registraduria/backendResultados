import certifi
import json
import pymongo
from typing import Generic, TypeVar


T = TypeVar('T')


class InterfaceRepository(Generic[T]):

    def __init__(self):
        ca = certifi.where()
        data_config = self.load_file_config()
        client = pymongo.MongoClient(data_config.get("db-connection"), tlsCAFile=ca)

    def load_file_config(self):
        with open("../config.json") as file:
            data = json.load(file)

        return data
