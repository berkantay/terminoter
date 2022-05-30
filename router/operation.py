
from note.note import Note
from datetime import datetime
import json
import os
import screens
import parse






class OperationManager(Note):
    def __init__(self):
        self.auth_success=False
        self.credential_file_name= ".credentials.json"
        self.credentials = {
                    "username" : "", \
                    "password" : "", \
                    }


    def fillNoteData(self,inputs:tuple):
        now = datetime.now()

        note=Note(inputs[0], inputs[1], now.strftime("%d.%m.%Y"), inputs[2])
        
        return note


    def checkAuth(self):
        file_exists = os.path.exists(self.credential_file_name)

        if not file_exists or not self.validAuth():
            self.auth_success = False
        else:
            self.auth_success = True
        
        return self.auth_success
            


    def getCredentials(self):

        file=open(self.credential_file_name, 'r')

        data = json.loads(file.read())

        username = data ['username']
        password = data ['password']

        return username,password



    def validAuth(self):

        username, password = self.getCredentials()
        is_valid = False
        if username == "" and password == "":
            is_valid = False

        else:
            is_valid = True

        return is_valid



    def generateCredentialsJson(self):
        
        file=open(self.credential_file_name, 'w')
        username, password = screens.authScreen()
        
        self.credentials={"username" : username , "password": password}
        credentials_json = json.dumps(self.credentials, indent = 4)
        file.write(credentials_json)
        
        file.close()



        
            


    # def getAuth(self):
        
    #         f= open(credential_file_name, "r")
    #         print("Please authorize using "+  '\033[95m'+ "terminoter auth command" + '\033[0m')



