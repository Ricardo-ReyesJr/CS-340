from pymongo import MongoClient
from bson.objectid import ObjectId


    
class AnimalShelter (object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:39329/test?authSource=AAC'%("aacuser", "aacuser"))
        self.database = self.client['AAC']
        # This creates the method to implement the C in CRUD
    
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert!=0:
                return True
            else:
                return False    
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
            
            # This creates the method to implement the R in CRUD

    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria,{"_id": False})
            for document in data:
                print(document)
            
        else:
            data = self.database.animals.find({},{"_id": False})
        
        return data
    
    # This creates the method to implement the U in CRUD
    def update(self, initial, change):
        if initial is not None:
            if self.database.animals.count.documents(initial, limit = 1) != 0:
                update_results = self.database.animals.update_many(initial, {"$set" : change})
                result = update_results.raw_result
            else:
                result = "Document is not available"
            return result
        else:
            raise Exception("Nothing to update, parameter is empty")
        
    # This creates the method to implement the D in CRUD
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) !=0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                result = "Document is not available"
            return result
        else:
            raise Exception("Nothing to update, parameter is empty")
