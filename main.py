
from bson import ObjectId
from data.data import Database
from note.note import Note
import parse
import sys
from router.operation import OperationManager



def main():

    db=Database()
    operation_manager = OperationManager()
    note = Note()

    if not parse.checkCommand(sys.argv):
        exit("Invalid argument count")

    data,option=parse.issueCommand(sys.argv[1])

    if not data and option == None:
        exit("Unknown terminator command")
    

    res=operation_manager.checkAuth()

    if not res:
        operation_manager.generateCredentialsJson()


    cred=operation_manager.getCredentials()

    client=db.authDatabase(cred[0], cred[1])

    if client != None:
        collections=db.listCollections(client,'Notes',False)
    else:
        exit()

    if option == parse.OperationOption.ADD: #add command

        if not parse.checkDate(data[2]):
            exit("Invalid date input.")

        note=operation_manager.fillNoteData(data)
        note.addTask(db, collections["tasks"])

    elif option == parse.OperationOption.REMOVE:

        db.deleteCollectionContent(collections["tasks"], ObjectId(data))
        print("Current task list:")
        db.listCollectionsContent(collections["tasks"])
        
    elif option == parse.OperationOption.LIST:

        print("Total task count is {}".format(db.getCollectionContentCount(collections["tasks"])))
        db.listCollectionsContent(collections["tasks"])

        
            
    else :
        exit("go away!")


if __name__ == "__main__":
    main()