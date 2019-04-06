# os.makedirs(path, exist_ok=True)
import os
import shutil
from library import category

# DEBUG for now:
__file__ = os.getcwd()+'\\simple-file-sort'

# Main function - only called if opened
if __name__ == '__main__':
    print('Sorting Files... \n You may be asked to select a category for each file, you can add your own, or select from already given')

    # For now only works on script directory
    dir = os.path.dirname(__file__)

    categories = get_categories()
    print(dir)
    for file in os.listdir(dir):
        if os.path.isfile(file):

            if '.' in file:
                destination_folder = category.choose_category(file)
            else: # Problem 1: File has no extension
                destination_folder = 'NO EXTENSION'

            print(file)
        #shutil.move(dir+file, destination_folder)
