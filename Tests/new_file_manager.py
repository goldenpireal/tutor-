import os 


class FileManager:
    def __init__(self): #creates the project root
        
        self.project_root = os.path.dirname(os.path.dirname(__file__)) 

    def path_builder(self, relative_path): #creates the full path from relative path
        
        path = os.path.join(self.project_root, relative_path) 
        return path

    def exists ( self, relative_path ): #checks if a file / dir exists (returns boolean)
        
        full_path = self.path_builder(relative_path)
        return os.path.exists(full_path)
    
    def _ensure_directory (self, relative_path): #uses the exists to decide whether to create a new file/ dir
        
        parent_path = os.path.dirname(self.path_builder(relative_path))        
        os.makedirs(parent_path, exist_ok=True)

    def write(self, relative_path, contents):
        
        full_path = self.path_builder(relative_path) #added to avoid using the path_builder again and again
        self._ensure_directory(relative_path) #ensures whether the file exists before proceeding and creates it
        with open (full_path, "w") as file: # over-writes / writes new contents to the file
            file.write (contents)
    
    def read(self, relative_path):# for reading a specific file with it's relative_path

        full_path = self.path_builder(relative_path)
        with open(full_path, 'r') as file:
            content = file.read()
        return content







'''
#This section is for figuring out the project_root
#it is a bit faulty because moving the file_manager can break it 
#But works for now...
def project_root_finder():
    return os.path.dirname(os.path.dirname(__file__))

project_root = project_root_finder()




#This section is for check whether a file/folder exists or not
#It takes the input of a relative path wrt the path folder then the program
#adds the project root from the project_root_finder function.
def path_builder(relative_path):
    path = os.path.join(project_root, relative_path)
    return path

def exists ( relative_path ):
    full_path = path_builder(relative_path)
    return os.path.exists(full_path)
    '''