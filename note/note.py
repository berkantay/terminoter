from data.data import Database
import pymongo

class Note(Database):

    def __init__(self, owner:str=None, task:str = None, creationDate = None, deadline = None):
        self.owner = owner
        self.task = task
        self.creationDate = creationDate
        self.deadline = deadline
        
        self.task = {
                    "owner" : self.owner , \
                    "task" : self.task, \
                    "creation_date" : self.creationDate , \
                    "deadline" : self.deadline
                    }


    def addTask(self, db:Database, collection:pymongo.database.Database):
        db.insertData(collection,self.task)




        
