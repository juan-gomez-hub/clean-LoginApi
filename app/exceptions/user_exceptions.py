

class userAlreadyExists(Exception):
    pass


class missingFields(Exception):
    def __init__(self, missingFields):
        self.missingFields = missingFields
        super().__init__(f"{', '.join(missingFields)}")


class thisUserNotExist(Exception):
    pass


class tokenInvalid(Exception):
    pass


class passwordIncorrect(Exception):
    pass
