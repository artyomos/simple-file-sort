import os

# DEBUG for now:
__file__ = os.getcwd()+'\\simple-file-sort'

FIRST_LINE = '(DO NOT EDIT) Simple File Sort Category File\n'

categories = {}

def get_categories():
    dir = os.path.dirname(__file__) + '\\library\\categories'

    # Make the category directory if it doesn't exist
    os.makedirs(dir, exist_ok=True)
    for file in os.listdir(dir):
        #print(file)
        #print(file.endswith('.cat'))
        if file.endswith('.cat'):
            with open(dir+ '\\' + file, 'r') as owo:
                if owo.readline() == FIRST_LINE:
                    for line in owo:
                        # line[:-1] to remove newline char
                        line = line[:-1]
                        try:
                            # Get category and items
                            category, items = line.split(' = ')
                            items = items.split(',')
                            if category in categories:
                                print('Warning: Overwriting category already set.')
                            categories[category] = items
                            print(category, items)
                        except ValueError:
                            # Invalid line, ignore for now
                            print('WARNING: Invalid line in file {}, if you haven\'t edited the file, report this error to the developer (Along with the file!)'.format(file))
                        except Exception as e:
                            print('Error: {}'.format(e))
                        # print(line)
                else: print('doop')
get_categories()
def make_category(category):
    pass

def update_category(new_extension, category):
    pass

def write_categories():
    pass

def choose_category(file):
    pass
