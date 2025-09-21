import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from app.entities.user import User
from dotenv import load_dotenv
import os

load_dotenv(override=True)


class DatabaseConnection:
    def __init__(self, testing=False):
        self.testing = testing
        self.database = os.getenv("DB_DATABASE") or "test"
        self.host = os.getenv("DB_HOST") or "localhost"
        self.user = os.getenv("DB_USER") or "postgres"
        self.password = os.getenv("DB_PASSWORD") or ""
        self.port = os.getenv("DB_PORT") or 5432
        # self.config = Config()

    @contextmanager
    def get_connection(self):
        conn = None
        try:
            if not self.testing:
                host = self.host
                port = self.port
                database = self.database
                user = self.user
                password = self.password
                cursor_factory = RealDictCursor

            else:
                host = "localhost"
                port = 5432
                database = "test"
                user = "postgres"
                password = "195418"
                cursor_factory = RealDictCursor
            conn = psycopg2.connect(host=host, port=port, database=database,
                                    user=user, password=password,
                                    cursor_factory=cursor_factory)
            yield conn
            # with conn as cursor:

        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if conn:
                conn.close()

    def execute_schema(self, schema_path):
        with self.get_connection() as conn:
            with open(schema_path, "r", encoding="utf-8") as f:
                sql_code = f.read()
                with conn.cursor() as cur:
                    cur.execute(sql_code)
                conn.commit()

    def query_CreateUser(self, user: User):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""INSERT INTO loginapi(email,username,passhashed)
                    values(%s,%s,%s)""",
                            (user.email, user.username, user.passHashed))

    def leer(self):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM loginapi;")
                for prueba in cur:
                    print(
                        f"""id: {prueba.__getitem__('id')} email:
                        {prueba.__getitem__('email')}
                        username: {prueba.__getitem__('username')}""")
