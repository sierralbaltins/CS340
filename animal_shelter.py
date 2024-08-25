from pymongo import MongoClient
from bson.objectid import ObjectId

class NewAnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """
   
    def __init__(self, username, password, client, port, database, collection):
        # Initialize MongoDB client and connect to the database and collection
        self.client = MongoClient(f'mongodb://{username}:{password}@{client}:{port}')
        self.database = self.client[database]
        self.collection = self.database[collection]

    # Create method to implement the C in CRUD
    def create(self, data):
        if data:
            self.collection.insert_one(data)  # data should be a dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method to implement the R in CRUD
    def read(self, query=None):
        if query is None:
            query = {}
        return list(self.collection.find(query))

    # Update method to implement the U in CRUD
    def update(self, query, update_data):
        if query and update_data:
            update_result = self.collection.update_many(query, {'$set': update_data})
            return update_result.modified_count
        else:
            raise Exception("Query or update data is missing")

        if '_id' in df.columns:
            df = df.drop(columns=['_id'])

    # Delete method to implement the D in CRUD
    def delete(self, query):
        if query:
            delete_result = self.collection.delete_many(query)
            return delete_result.deleted_count
        else:
            raise Exception("Nothing to delete, query parameter is empty")