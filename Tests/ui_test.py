#This UI is for taking in input while user is logging a new session
from memeory_manager_test import MemoryManager
from new_file_manager import FileManager as fm
    
data = input()

def file_exists_error_ui (relative_path, subject, topic):

    print("File/ Folder not found!(If not expected watch for typos!!)")
    print("Do you wanna proceed with the file/ folder creation ({subject}/{topic})")
    permission = input("Y/n").lower()

    if permission == "n":
        print("Permission denied")

    elif permission != "n" & permission != "y":
        print("input Y/n")
    
    else:
        MemoryManager.data_manager(data, permission)






