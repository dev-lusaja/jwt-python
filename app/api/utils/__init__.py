import yaml


def load_config(path_file):
    file_object = open(path_file)
    return yaml.load(file_object)
