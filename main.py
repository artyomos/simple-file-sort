import os
import shutil
from library import backend

# DEBUG for now:
__file__ = os.getcwd()+'\\simple-file-sort'

# Main function - only called if opened
if __name__ == '__main__':
    print('Sorting Files... \n You may be asked to select a category for each file, you can add your own, or select from already given')
    print('Please note EVERY FILE will be moved to a folder, so BE CAREFUL HOW YOU USE THIS')
    input('Press ENTER to continue... or close this window to cancel')

    # For now only works on script directory
    dir = os.path.dirname(__file__)

    categories = backend.get_categories()
    print(dir)
    for file in os.listdir(dir):
        if os.path.isfile(file):
            if '.' in file:
                extension = file.split('.')[-1]
                try:
                    destination_folder = categories[extension]
                except KeyError:
                    while True:
                        print('\nUh oh! Found an extension (.{}) that isn\'t in any category! \nWhat would you like to do with it?'.format(extension))
                        result = input('Please type only what is shown:\n1. Ignore and leave it\n2.Define a category for it')
                        if result == '1':
                            backend.add_extension(categories, 'IGNORE', extension)
                            destination_folder = 'IGNORE'
                            break
                        elif result == '2':
                            while True:
                                category = input('\nPlease define the category for this file as such: "example"\nFile Category:)').lower()
                                verify = input('Please verify that you wish for the file extension {}\'s category to be defined as {} (Y/N)'.format(extension, category))
                                if verify == 'y':
                                    backend.add_extension(categories, category, extension)
                                    destination_folder = categories[extension]
                                elif verify == 'n':
                                    print('Ok, going back to previous question')
                                else:
                                    print('Type what is shown please')
                                break
                            break
                        else:
                            print('Very funny. Try again.')

            else: # Problem 1: File has no extension
                destination_folder = 'NO EXTENSION'

            print(file, destination_folder)
            if destination_folder == 'IGNORE': pass
            else:
                print('Moved {} to folder {}'.format(file, destination_folder))
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(dir+ '\\'+file, destination_folder+'\\')
    print('All file sorting finished. Writing categories..')
    backend.write_categories(categories)
    input('Done. Press ENTER to close...')
