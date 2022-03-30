import datetime
import jwt

from app.models.BlackListToken import BlacklistToken
'''
    /auth/register
    /auth/login
    /auth/logout
    /auth/user
'''
def encode_auth_token(user_id, SECRET):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            SECRET,
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token, SECRET):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, SECRET)

        is_blacklisted_token = check_blacklist(auth_token)
        if is_blacklisted_token:
            return {'status': 'error', 'message':'Token expired. Please log in again.'}            

        return {'status': 'success', 'user_id': payload['sub']}
    except jwt.ExpiredSignatureError:
        return {'status': 'error', 'message':'Signature expired. Please log in again.'}
    except jwt.InvalidTokenError:
        return {'status': 'error', 'message':'Invalid token. Please log in again.'}


def check_blacklist(auth_token):
    # check whether auth token has been blacklisted
    res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
    if res:
        return True
    else:
        return False

def add_to_blacklist(auth_token):
    blacklist = BlacklistToken(token=auth_token)
    blacklist.save()