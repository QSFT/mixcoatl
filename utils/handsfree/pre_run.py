import os
import sys
import json

def validate_input(update_file):
    """
    This method validates the input file. Returns true if the JSON is valid, false
    otherwise.
    """
    try:
        json.load(open(update_file))
        return True
    except ValueError:
        exit(-1)
        return False


def find_essential_files(setup_dir):

    print ""

    print "\n[Finding essential files]\n"

    if os.path.isdir(setup_dir):
        print "Setup directory exists."
        setup_directory_test = True
    else:
        print "Cannot find setup directory. You specified: {}.\n" \
              "Exiting for safety reasons".format(setup_dir)
        sys.exit(97)

    if os.path.isfile(setup_dir+'/users/initial-account.json'):
        print "Found initial-account.json.",
        if validate_input(setup_dir+'/users/initial-account.json'):
            print "It contains VALID JSON."
            initial_account_test = True
        else:
            print "It contains INVALID JSON. Exiting for safety reasons."
            sys.exit(99)
    else:
        print "Could not find {}/users/initial-account.json. This won't work. Exiting for safety reasons.".format(setup_dir)
        sys.exit(98)

    if os.path.isfile(setup_dir+'/clouds/initial_cloud.json'):
        print "Found initial_cloud.json.",
        if validate_input(setup_dir+'/clouds/initial_cloud.json'):
            print "It contains VALID JSON."
            initial_cloud_test = True
        else:
            print "It contains INVALID JSON. Exiting for safety reasons."
            sys.exit(99)
    else:
        print "Could not find {}/clouds/initial_cloud.json. This won't work. Exiting".format(setup_dir)
        sys.exit(98)

    return setup_directory_test, initial_account_test, initial_cloud_test

def parse_descriptors_and_credentials(setup_dir):

    cloud_descriptors_dir = '{}/clouds/descriptors'.format(setup_dir)
    cloud_credentials_dir = '{}/clouds/credentials'.format(setup_dir)

    num_descriptors = len([name for name in os.listdir(cloud_descriptors_dir) if os.path.isfile(cloud_descriptors_dir+'/'+name)])
    num_credentials = len([name for name in os.listdir(cloud_credentials_dir) if os.path.isfile(cloud_credentials_dir+'/'+name)])

    print "\nFound {} cloud descriptor files for the following clouds:\n".format(num_descriptors)

    print "{:30} {:50} {:8}".format("Name", "Endpoint", "Cloud ID")
    print "{:30} {:50} {:8}".format("----", "--------", "--------")
    for cloud_descriptor in os.listdir(cloud_descriptors_dir):
        descriptor_json = json.load(open(cloud_descriptors_dir+'/'+cloud_descriptor))
        friendly_name, endpoint_url, cloud_id = descriptor_json['friendly_name'], descriptor_json['endpoint_url'], descriptor_json['cloud_id']
        print "{:30} {:50} {:8}".format(friendly_name, endpoint_url, cloud_id)
        is_valid = validate_input('{}/clouds/descriptors/'.format(setup_dir)+cloud_descriptor)

    print "\nFound {} cloud credential files for the following clouds:\n".format(num_credentials)

    print "{:30} {:8}".format("Name", "Cloud ID")
    print "{:30} {:8}".format("----", "--------")
    for cloud_credential in os.listdir(cloud_credentials_dir):
        credential_json = json.load(open(cloud_credentials_dir+'/'+cloud_credential))
        name, cloud_id = credential_json['addAccount'][0]['name'], credential_json['addAccount'][0]['cloudSubscription']['cloudId']
        print "{:30} {:8}".format(name, cloud_id)

def pretty_print_setup_dir(setup_dir):
    '''
    Pretty print the directory structure of the setup directory
    '''

    for root, dirs, files in os.walk(setup_dir):
        level = root.replace(setup_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

def dry_run(setup_dir):
    '''
    Lists things that will be done as part of the install.
    :return:
    '''

    find_essential_files(setup_dir)

    cloud_descriptors_dir = '{}/clouds/descriptors'.format(setup_dir)
    cloud_credentials_dir = '{}/clouds/credentials'.format(setup_dir)

    parse_descriptors_and_credentials(setup_dir)

    for cloud_descriptor in os.listdir(cloud_descriptors_dir):
        is_valid = validate_input('{}/clouds/descriptors/'.format(setup_dir)+cloud_descriptor)

    for cloud_credential in os.listdir(cloud_credentials_dir):
        is_valid = validate_input('{}/clouds/credentials/'.format(setup_dir)+cloud_credential)
