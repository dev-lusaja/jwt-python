import falcon
import yaml

from api import load_handlers


class Wsgi:
    def __init__(self):
        stream = open('api/routes.yml', 'r')
        self.api = falcon.API()
        self.routes = yaml.load(stream)
        self.load_routes()

    def load_routes(self):
        base = self.routes['routes']['base']
        templates = self.routes['routes']['templates']
        handlers = load_handlers()
        for template in templates:
            url = template['url']
            handler = template['handler']
            self.api.add_route(url % base, handlers[handler])

