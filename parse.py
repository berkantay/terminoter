import screens
import enum
import string
from datetime import datetime


@enum.unique
class OperationOption(enum.Enum):
    # Would like to use enum.auto(), but it's only available in >= 3.6
    ADD = 1
    REMOVE = 2
    LIST = 3



def checkDate(date:string) -> bool:


    if datetime.strptime(date, '%d.%m.%Y'):
        return True
    
    else:
        return False


def checkCommand(args:list) -> bool:

    if len(args) != 2:
        return False
    return True


def issueCommand(arg:str):
    

    inputs=()
    option=None

    if arg == "add":
    
        inputs = screens.taskAdditionScreen()
        option = OperationOption.ADD
    
    elif arg ==  "remove":
    
        inputs =  screens.removeTaskScreen()
        option = OperationOption.REMOVE
    
    elif arg == "list":
    
        screens.taskListingScreen()
        option = OperationOption.LIST

    return inputs, option






