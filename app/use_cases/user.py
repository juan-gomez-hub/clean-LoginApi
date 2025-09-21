import requests
from app.entities.user import User
from app.infrastructure.repository.userRepository import UserRepository
from app.utils.validation import validateUsername, validationEmail, validationPassword
from app.infrastructure.services.jwt_service import generate_token
from app.exceptions.user_exceptions import passwordIncorrect, userAlreadyExists, thisUserNotExist
import bcrypt

class createUserUseCase:
    def __init__(self,userRepository:UserRepository):
        #self.repository=userRepository
        self.user_repository = userRepository  # renombrado para coincidir
    
    def findUser(self,usernameToFind):
        return self.user_repository.findByUsername(usernameToFind)


    def execute(self, fieldUsername: str, fieldEmail: str, fieldPassword: str):
        userToCreate = User(fieldUsername, fieldEmail,fieldPassword)
        validateUsername(userToCreate.username)
        validationEmail(userToCreate.email)
        validationPassword(userToCreate.passHashed)

        existInDb=self.findUser(userToCreate.username)
        passwordBytes= fieldPassword.encode("utf-8")
        userToCreate.passHashed=(bcrypt.hashpw(passwordBytes,bcrypt.gensalt(12))).decode()
        if existInDb:
            raise userAlreadyExists
        # Guardar en DB mediante el repositorio
        userCreated=self.user_repository.save(userToCreate)
        return userCreated
    

class LoginUserUseCase:

    def __init__(self,userRepository:UserRepository):
        self.user_repository=userRepository

    def execute(self,usernameField:str,passwordField:str):
        validateUsername(usernameField,login=True)
        validationPassword(passwordField)
        existInDb=self.user_repository.findByUsername(usernameField)
        if not existInDb:
            raise thisUserNotExist
        passHashed=self.user_repository.getPassword(usernameField)
        
        passHashed=passHashed.encode("utf-8")
        passwordField=passwordField.encode("utf-8")
        if not bcrypt.checkpw(passwordField,passHashed):
            raise passwordIncorrect
        token=generate_token({"role":1})
        return token

