from app.entities.user import User
from app.infrastructure.db.db_connect import DatabaseConnection
from app.infrastructure.repository.userRepositoryInterface import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def __init__(self):
        self.db_conn = DatabaseConnection()

    def save(self, user: User):
        with self.db_conn.get_connection() as conn:   # ✅ abre la conexión
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO loginapi (username, email, passhashed) VALUES (%s, %s, %s)",
                    (user.username, user.email, user.passHashed),
                )
                conn.commit()
        return user

    def findByUsername(self, username):
        with self.db_conn.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT username FROM loginapi WHERE username=%s ", (username,))
                retorno = cursor.fetchone()
                return retorno['username'] if retorno else None

    def getPassword(self, username):
        try:
            with self.db_conn.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT passhashed FROM loginapi WHERE username=%s ", (username,))
                    retorno = cursor.fetchone()
                    return retorno['passhashed'] if retorno else None
        except Exception as e:
            print(e)

    def killToken(self, token):
        try:
            with self.db_conn.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO blacklist(token) VALUES(%s)", (token,))
                    conn.commit()
        except Exception as e:
            print(e)
