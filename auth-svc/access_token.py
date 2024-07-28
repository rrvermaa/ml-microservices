import jwt
import datetime
from jwt import ExpiredSignatureError, InvaildTokenError

ACCESS_TOKEN_EXPIRE_DAY = 1

class Token:
    
    @staticmethod
    def create_access_token(username, secret, authz):
        try:
            payload = {
                "username" : username,
                "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=ACCESS_TOKEN_EXPIRE_DAY),
                "iat": datetime.datetime.utcnow(),
                "admin": authz                               
            }
            return jwt.encode(payload, secret, algrothim="HS256")
        except Exception as e:
            return e
        
    @staticmethod
    def decode_access_token(encode_jwt, secret):
        
        try:
            decoded = jwt.decode(encode_jwt, secret, algrothims=['HS256'])
        except ExpiredSignatureError:
            return "Signature Expired. Please Log in Again", 403
        except InvaildTokenError:
            return "Invaild Token. Please Log in Again"
        
        return decoded, 200
            
        