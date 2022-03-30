from flask import jsonify

class FailedLoginException(Exception):
    
    def __init__(self, message, status_code=401, payload=None):
        Exception.__init__(self)
        self.message = message        
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

