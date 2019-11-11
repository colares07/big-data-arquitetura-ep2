from pymongo import MongoClient

class DatabaseMongo:
    def __init__(self, database='db', host='localhost', port=27017):
        self.database = database
        self.client = MongoClient(host=host, port=port)
        self.db = self.client[self.database]

    def add(self, collection='collection', json={}):
        return self.db[collection].insert_one(json).inserted_id
    
    def get(self, collection='collection', find={}):
        return self.db[collection].find(find)