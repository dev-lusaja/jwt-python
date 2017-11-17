import falcon

from api import load_handlers
from api.utils import load_config


class Wsgi:
    def __init__(self):
        self.api = falcon.API()
        self.routes = load_config('api/routes.yml')
        self.load_routes()

    def load_routes(self):
        base = self.routes['routes']['base']
        templates = self.routes['routes']['templates']
        handlers = load_handlers()
        for template in templates:
            url = template['url']
            handler = template['handler']
            self.api.add_route(url % base, handlers[handler])
