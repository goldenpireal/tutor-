import json
from new_file_manager import FileManager
import ui_test


class MemoryManager:

    def __init__(self):
        self.fm = FileManager()

    def data_manager(self, data, permission):
        

        subject = data.get("subject")
        topic = data.get("topics")
        sections = data.get("sections")
        overwrite = data.get("overwrite", False)

        relative_path = f"Dynamic/{subject}/{topic}.json"

        #full_path = self.fm.path_builder(relative_path)
    
        if self.fm.exists(relative_path) == True:
            file_folder_found = True
            
        
        else :

            file_folder_found = False
            '''print (f"The folder/ file {subject}, {topic} not found")
            permission = (input ("Do you wanna contintue with creation(Y/n):")).lower()
'''
            while self.fm.exists(relative_path) == False:
                try:
                    if permission == "y":
                        self.fm._ensure_directory(relative_path)
                
                    elif permission =="n":
                        pass

                    else:
                        pass

                except ValueError:
                    print("Invalid input")
        

        #The rest of the code is writing and appending.. 







