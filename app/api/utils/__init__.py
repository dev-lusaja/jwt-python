# -*- coding: utf-8 -*-
import yaml


def load_file(path_file):
    file_object = open(path_file)
    return yaml.load(file_object)
