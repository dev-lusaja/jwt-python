# -*- coding: utf-8 -*-
import falcon
import yaml
import importlib

from api import prefix
from api.utils import load_file


class Wsgi:
    def __init__(self):
        self.api = falcon.API()
        self.load_routes()

    def load_routes(self):
        for uri_tpl, resource in load_file('api/routes.yml').items():
            module_parts = resource.split('.')
            module_name = '.'.join(module_parts[:-1])
            module = importlib.import_module(module_name)
            Resource = getattr(module, module_parts[-1])
            resource_instance = Resource()
            self.api.add_route(prefix + uri_tpl, resource_instance)