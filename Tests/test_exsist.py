import os
from main import project_root
relative_path = input()

def path_builder(relative_path):
    path = os.path.join('', relative_path)
    return path

def exists ( relative_path ):
    full_path = path_builder(relative_path)
    return os.path.exists(full_path)



print(exists(relative_path)) #for testing the feature

