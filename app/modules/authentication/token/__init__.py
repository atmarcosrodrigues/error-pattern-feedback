import sys
sys.path.append(".") 


from app.modules.authentication.token.service import encode_auth_token, decode_auth_token, add_to_blacklist

'''
    Module token
'''

def encode(user_id, SECRET):
    return encode_auth_token(user_id, SECRET)

def decode(auth_token, SECRET):
    return decode_auth_token(auth_token, SECRET)
