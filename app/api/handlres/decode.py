import falcon
import jwt
import yaml


class DecodeHandler:
    def __init__(self):
        pass

    def on_get(self, req, resp, token):
        try:
            stream = open('setup.yml', 'r')
            params = yaml.load(stream)
            options = {
                'require_exp': True,
                'verify_exp': True
            }
            jwt_decode = jwt.decode(token, params['secret'], options=options, algorithm=params['token']['algorithm'])
            if jwt_decode is not None:
                resp.media = {'data': jwt_decode}
                resp.status = falcon.HTTP_200
            else:
                resp.media = {'data': ''}
                resp.status = falcon.HTTP_200
        except jwt.ExpiredSignatureError:
            resp.media = {'data': 'Signature has expired'}
            resp.status = falcon.HTTP_401
        except Exception, error:
            resp.media = {'data': 'Invalid token'}
            resp.status = falcon.HTTP_401
