import os

def dry_run(setup_dir):
    '''
    Lists things that will be done as part of the install.
    :return:
    '''

    # Pretty print the directory structure of the setup directory
    for root, dirs, files in os.walk(setup_dir):
        level = root.replace(setup_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

def sanity_check():
    '''
    Does a sanity check of the install arguments.
    :return:
    '''
    pass