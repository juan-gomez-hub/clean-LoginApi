import sys
import os

# agrega la raíz del proyecto (loginAPI) al PYTHONPATH
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
import pytest
# from app import create_app, db
from app.interface.web.flask_app import create_app
# from server import create_app, db

@pytest.fixture()
def app():
    app=create_app(True)
    # with app.app_context():
    #     try:
    #         db.create_all()
    #         print("[INFO] Base de datos creada exitosamente.")
    #     except Exception as e:
    #         print(f"[ERROR] Error al crear la base de datos: {e}")
    #         raise  # Relanza la excepción para que pytest lo detecte como un fallo.
    # # app.run()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
