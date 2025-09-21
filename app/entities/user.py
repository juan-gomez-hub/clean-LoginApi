

class User:
    username = str
    email = str
    passHashed = str

    def __init__(self, username="", email="", passHashed=""):
        self.username = username
        self.email = email
        self.passHashed = passHashed

    def __repr__(self):

        return f"""username: {self.username}\nemail: {self.email}"""
