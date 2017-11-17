import falcon
import jwt

from api.utils import load_config


class DecodeHandler:
    def __init__(self):
        params = load_config('setup.yml')
        self.token = params['token']
        self.secret = params['secret']

    def on_get(self, req, resp, token):
        try:
            options = {
                'require_exp': True,
                'verify_exp': True
            }
            jwt_decode = jwt.decode(token, self.secret, options=options, algorithm=self.token['algorithm'])
            if jwt_decode is not None:
                resp.media = {'data': jwt_decode}
                resp.status = falcon.HTTP_200
            else:
                resp.media = {'data': ''}
                resp.status = falcon.HTTP_200
        except jwt.ExpiredSignatureError:
            resp.media = {'data': 'Signature has expired'}
            resp.status = falcon.HTTP_401
        except Exception as error:
            resp.media = {'data': 'Invalid token'}
            resp.status = falcon.HTTP_401
