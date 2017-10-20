import falcon
import jwt


class EncodeResource:

    def on_post(self, req, resp):
        metadata = req.media.get('metadata')
        jwt_encoded = jwt.encode({'metadata': metadata}, 'secret', algorithm='HS256')
        resp.media = {'token': jwt_encoded}
        resp.status = falcon.HTTP_200


class DecodeResource:

    def on_get(self, req, resp, token):
        try:
            jwt_decode = jwt.decode(token, 'secret', algorithms=['HS256'])
            if jwt_decode is not None:
                resp.media = {'data': jwt_decode}
                resp.status = falcon.HTTP_200
            else:
                resp.media = {'data': ''}
                resp.status = falcon.HTTP_200
        except Exception:
            resp.media = {'error': 'invalid token'}
            resp.status = falcon.HTTP_500


api = falcon.API()
api.add_route('/v1/authorizations/', EncodeResource())
api.add_route('/v1/authorizations/{token}', DecodeResource())
