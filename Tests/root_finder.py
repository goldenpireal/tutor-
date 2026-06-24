import os

def root_find():
    return os.path.dirname(os.path.dirname(__file__))

project_root = root_find()