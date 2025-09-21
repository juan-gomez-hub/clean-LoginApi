from flask import jsonify, request

from app.exceptions.user_exceptions import passwordIncorrect, userAlreadyExists, missingFields, tokenInvalid, thisUserNotExist


class UserController:
    def __init__(self, create_use_case, login_use_case):
        self.create_use_case = create_use_case
        self.login_use_case = login_use_case

    def create_user(self):
        try:
            data = request.json
            fields_missing = []
            if not isinstance(data.get("username"), str):
                fields_missing.append("username")
            if not isinstance(data.get("email"), str):
                fields_missing.append("email")
            if not isinstance(data.get("password"), str):
                fields_missing.append("password")
            if fields_missing:
                raise missingFields(fields_missing)
            fieldUsername = data.get("username")
            fieldEmail = data.get("email")
            fieldPassword = data.get("password")

            user = self.create_use_case.execute(
                fieldUsername, fieldEmail, fieldPassword)
            return {"success": f"User {user.username} created"}

        except ValueError as ve:
            return {"Error": str(ve)}, 400
        except missingFields as e:
            return {"Error": "Missing or value incorrect on fields "+str(e)}, 400

        except userAlreadyExists:
            return {"Error": "User already exists"}

        except Exception as e:
            print(e)
            return {"Error": "Internal server error"}, 500

    def login(self):
        try:
            data = request.json
            fields_missing = []
            if not isinstance(data.get("username"), str):
                fields_missing.append("username")
            if not isinstance(data.get("password"), str):
                fields_missing.append("password")
            if fields_missing:
                raise missingFields(fields_missing)
            username = data.get("username")
            password = data.get("password")
            tokenUser = self.login_use_case.execute(username, password)
            if not tokenUser:
                raise tokenInvalid
            return {"Success": tokenUser}

        except ValueError as e:
            return {"Error": str(e)}, 401

        except passwordIncorrect:
            return {"Error": "Password incorrectly"}, 400
        except missingFields as e:
            return {"Error": "Missing fields "+str(e)}, 401
        except tokenInvalid:
            return {"Error": "Token is invalid"}, 401
        except thisUserNotExist:
            return {"Error": "This user not exist in the system"}, 400
        except Exception as e:
            print(e)
            return jsonify({"Error": "Internal Server Error"}), 500
