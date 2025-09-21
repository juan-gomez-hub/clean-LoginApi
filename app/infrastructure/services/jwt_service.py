import jwt


def generate_token(payload):
    encoded_jwt = jwt.encode({"some": payload}, "secret", algorithm="HS256")
    return encoded_jwt

def kill_token(token):
    pass