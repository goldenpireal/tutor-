from new_file_manager import FileManager
from memeory_manager_test import MemoryManager

def file_not_found_menu(relative_path):
    print (f"The folder/ file {subject}, {topic} not found")
    permission = (input ("Do you wanna contintue with creation(Y/n):")).lower()

    while MemoryManager.self.fm.exists(relative_path) == False:
        try:
            if permission == "y":
                MemoryManager.self.fm._ensure_directory(relative_path)
        
            elif permission =="n":
                print("Operation cancelled")

            else:
                print("Invalid input")

        except ValueError:
            print("Invalid input")