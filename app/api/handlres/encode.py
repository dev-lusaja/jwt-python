import datetime
import falcon
import jwt
import yaml

from falcon.media.validators import jsonschema
from api.schemas.user import UserSchema


class EncodeHandler:
    def __init__(self):
        stream = open('setup.yml', 'r')
        params = yaml.load(stream)
        self.token = params['token']
        self.secret = params['secret']
        self.date = datetime.datetime.utcnow() + datetime.timedelta(minutes=self.token['time'])

    @jsonschema.validate(UserSchema.get())
    def on_post(self, req, resp):
        try:
            metadata = req.media.get('metadata')
            jwt_encoded = jwt.encode(
                {'exp': self.date, 'metadata': metadata},
                self.secret,
                algorithm=self.token['algorithm'])
            resp.media = {'token': jwt_encoded}
            resp.status = falcon.HTTP_201
        except Exception, error:
            resp.media = error.message
            resp.status = falcon.HTTP_500

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_404
