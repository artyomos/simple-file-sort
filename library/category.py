import os

# DEBUG for now:
__file__ = os.getcwd()+'\\simple-file-sort'

FIRST_LINE = '(DO NOT EDIT) Simple File Sort Category File\n'

DIRECTORY = os.path.dirname(__file__) + '\\library\\categories'
def get_categories():
    categories = {}

    # Make the category directory if it doesn't exist
    os.makedirs(DIRECTORY, exist_ok=True)
    for file in os.listdir(DIRECTORY):
        #print(file)
        #print(file.endswith('.cat'))
        if file.endswith('.cat'):
            with open(DIRECTORY+ '\\' + file, 'r') as owo:
                if owo.readline() == FIRST_LINE:
                    for line in owo:
                        # line[:-1] to remove newline char
                        line = line[:-1]
                        if not line.startswith('//'):
                            try:
                                # Get category and items
                                category, items = line.split(' = ')
                                items = items.split(',')
                                if category in categories:
                                    print('WARNING: Overwriting category already set.')
                                categories[category] = items
                                # print(category, items)
                            except ValueError:
                                # Invalid line, ignore for now
                                print('WARNING: Invalid line in file {}, if you haven\'t edited the file, report this error to the developer (Along with the file!)'.format(file))
                            except Exception as e:
                                print('Error: {}'.format(e))
                            # print(line)
                else: print('doop')

    # This one-liner inverts the dictionary, offering the abilit to search for category based on file extension
    categories = {value: key for key in categories for value in categories[key]}
    return categories

def make_category(categories, category, file):
    extension = file.split('.')[-1]
    try:
        if category == categories[extension]:
            return False # Already made
        else:
            print('WARNING: Tried to define a new category to extension already defined in another category')
            return False
    except KeyError:
        categories[extension] = category
        return True # Category Created

def update_category(categories, new_extension, category):
    pass

def write_categories(categories):
    # Don't bother comprehending this dictionary comprehension it took me forever to figure out how to do :)))))
    # Original (wrong version)
    #categories = {categories[key]: [key for value in categories if categories[key] == categories[value]] for key in categories }
    categories = {categories[key]:[value for value in categories if categories[value] == categories[key]] for key in categories}
    for category in categories:
        with open(DIRECTORY+ '\\' + category.lower(), 'w') as owo:
            values = ','.join(categories[category])
            owo.write(FIRST_LINE)
            owo.write('//This is an example comment. Follow the form of this file when designing your own (Recommended: One category per file)\n//Example: user_category = fileext,fileext,fileext [NO SPACES] \n')
            owo.write(f'{category} = {values}\n')
    return categories

def test_functions():
    print('Testing get_categories:')
    print(get_categories())

    print('Testing write_categories:')
    print(write_categories(categories))
    
test_functions()
