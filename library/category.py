import os

# DEBUG for now:
__file__ = os.getcwd()+'\\simple-file-sort'

def get_categories():
    dir = os.path.dirname(__file__)
    for file in os.listdir(dir):
        if os.path.isfile(file) and file.endswith('.cat'):
            pass

def make_category(category):
    pass

def update_category(new_extension, category):
    pass

def write_categories():
    pass

def choose_category(file):
    pass
