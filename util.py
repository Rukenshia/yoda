import os.path
import yaml
import chalk

# if folder does not exist, create it
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

# asks if you want to overwrite the given file, if it exists
def ask_overwrite(file_path):
    if os.path.isfile(file_path):
        chalk.red('A configuration file already exists. Are you sure you want to overwrite it? (y/n)')
        overwrite_response = raw_input().lower()
        if not (overwrite_response == 'y' or overwrite_response == 'yes'):
            return True
        return False
    return False

# inputs dict into a .yaml file
def input_data(data, file_path):
    with open(file_path, 'a') as config_file:
        yaml.dump(data, config_file, default_flow_style=False)

# get folder path from file path
def get_folder_path_from_file_path(file_path):
    return os.path.dirname(file_path)

# convert tuple to string
def tuple_to_string(input):
    if input:
        test_string = ''
        for i in input:
            test_string += (i + ' ')
        return test_string.lower().strip()
