# -*- coding: utf-8 -*-
import datetime
import falcon
import jwt


from falcon.media.validators import jsonschema
from api.schemas.metadata import MetadataSchema
from api.utils import load_file


class EncodeHandler:
    def __init__(self):
        params = load_file('setup.yml')
        self.token = params['token']
        self.secret = params['secret']

    @jsonschema.validate(MetadataSchema.get())
    def on_post(self, req, resp):
        try:
            date = datetime.datetime.utcnow() + datetime.timedelta(minutes=self.token['time'])
            metadata = req.media.get('metadata')
            jwt_encoded = jwt.encode(
                {'exp': date, 'metadata': metadata},
                self.secret,
                algorithm=self.token['algorithm'])
            resp.media = {'token': jwt_encoded}
            resp.status = falcon.HTTP_201
        except Exception as error:
            resp.media = error.message
            resp.status = falcon.HTTP_500

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_404
