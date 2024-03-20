
from pymongo import MongoClient


class ConnnectMongoDb:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['ECommerce']
        self.collection = self.db['Events']

    def insert(self, data):
        self.collection.insert_one(data)

    def find(self, data):
        return self.collection.find(data)

    def find_one(self):
        return self.collection.find_one()

    def update(self, data, new_data):
        self.collection.update_one(data, new_data)

    def delete(self, data):
        self.collection.delete_one(data)

