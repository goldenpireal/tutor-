import os

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