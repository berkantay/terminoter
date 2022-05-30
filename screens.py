import getpass


def taskAdditionScreen():

    print("Fill the information")
    
    owner = input("Owner:")
    task = input ("Task:")
    deadline = input("Deadline:")
    
    return owner, task, deadline

def authScreen():

    print("Fill the information")
    
    username = input("Username:")
    password = getpass.getpass("Password:")
    
    return username, password



def taskListingScreen():
    print("Tasks:")


def removeTaskScreen():
    return input("Please enter the task ID: ")
    

    
