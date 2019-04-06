import os
import shutil
from library import backend

# Main function - only called if opened
if __name__ == '__main__':
    while True:
        path = input('What is the path for the directory: ').strip()
        if os.path.isdir(path):
            break
        else:
            print('The path you gave was invalid! Make sure you are typing it properly...\n')
    print('\nSorting Files in {}... \n\nYou may be asked to select a category for unknown file extensions'.format(path))
    print('Please note EVERY FILE will be moved to a folder, so BE CAREFUL HOW YOU USE THIS')
    input('\nPress ENTER to continue... or close this window to cancel ')

    # For now only works on script directory
    dir = path

    categories = backend.get_categories()
    for file in os.listdir(dir):
        if os.path.isfile(dir+'\\'+file):
            if '.' in file:
                extension = file.split('.')[-1].lower()
                try:
                    destination_folder = categories[extension]
                except KeyError:
                    while True:
                        print('\nUh oh! Found an extension (.{}) that isn\'t in any category! \nWhat would you like to do with it?'.format(extension))
                        result = input('Please type only what is shown:\n1. Ignore and leave it\n2. Define a category for it\nChoice: ')
                        print('')
                        if result == '1':
                            backend.add_extension(categories, 'IGNORE', extension)
                            destination_folder = 'IGNORE'
                            break
                        elif result == '2':
                            while True:
                                category = input('\nPlease define the category for this file as such: "example"\nFile Category: ').lower()
                                verify = input('Please verify that you wish for the file extension .{}\'s category to be defined as {}\n(Y/N): '.format(extension, category))
                                if verify == 'y':
                                    backend.add_extension(categories, category, extension)
                                    destination_folder = categories[extension]
                                elif verify == 'n':
                                    print('Ok, going back to previous question')
                                else:
                                    print('Type what is shown please')
                                print('')
                                break
                            break
                        else:
                            print('Very funny. Try again.')
            else: # Problem 1: File has no extension
                destination_folder = 'NO EXTENSION'

            # Uncomment to debug current working file
            # print(file, destination_folder)
            if destination_folder == 'IGNORE': pass
            else:
                print('Moved {} to folder {}'.format(file, destination_folder))
                os.makedirs(dir+ '\\'+destination_folder, exist_ok=True)
                shutil.move(dir+ '\\'+file, dir+ '\\'+destination_folder+'\\')
    print('\nAll file sorting finished. Writing categories..')
    backend.write_categories(categories)
    input('Done. Press ENTER to close...')
