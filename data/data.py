from datetime import datetime
from bson import ObjectId
import pymongo
from urllib.parse import quote_plus
import json
from simplejson import dumps
from colorama import Fore, Back, Style

    

class Database:
    def __init__(self):
        self.collection=None
        self.count = 0

    def authDatabase(self,username,passwd):
        
        password = quote_plus(passwd)
        username = quote_plus(username)
        uri = "mongodb+srv://" + username + ":" + password + "@events.bshw9.mongodb.net/?retryWrites=true&w=majority"

        client = pymongo.MongoClient(uri)
        
        try:
            client.list_database_names()
            print('Database Connection Successfull...')

        except pymongo.errors.OperationFailure as err:
            print(f"Database Connection failed. Error: {err}")
        
        return client

    
    def listAllDatabases(self, client:pymongo.MongoClient):

        db =  list(client.list_databases()) #Database name
        json_db = dumps(db)
        databases=json.loads(json_db)

        for entries in databases:
            print(entries['name'])



    def listCollections(self, client:pymongo.MongoClient, db_name:str, hide=False):

        self.collection=client[db_name]
        
        if hide:
            for c in self.collection.list_collection_names():
                print(c)

        return self.collection


    def listCollectionsContent(self, collections:pymongo.database.Database):
        
        for index,content in enumerate(collections.find()):

            remainingTime = datetime.strptime(content['deadline'], '%d.%m.%Y') - datetime.today()
            print(Fore.BLACK + Back.LIGHTYELLOW_EX +"{}) {}\n".format(index, content["_id"]))
            print(Fore.GREEN + Back.RESET+ "Task: \t{} until {}.".format(content['task'], content['deadline']))
            print(Fore.WHITE + Back.RED + "\t{} hours left.".format(remainingTime))
            print(Style.RESET_ALL)
    
        return content

    def insertData(self,collection:pymongo.database.Database,note:dict):
        collection.insert_one(note)

    def getCollectionContentCount(self,collections:pymongo.database.Database):

        cursor = collections.find()

        return len(list(cursor))

    def deleteCollectionContent(self, collections:pymongo.database.Database, objInstance:ObjectId):
        
        query = {"_id" : objInstance}
        collections.delete_many(query)






# |"" {} until {}. | {} hours left".format(index ,content['_id'], content['task'], content['deadline'], remainingTime))