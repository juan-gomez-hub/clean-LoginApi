import pytest
from app.interface.web.flask_app import create_app


@pytest.fixture()
def app():

    app = create_app(testing=True)
    # with app.app_context():
    #     try:
    #         db.create_all()
    #         print("[INFO] Base de datos creada exitosamente.")
    #     except Exception as e:
    #         print(f"[ERROR] Error al crear la base de datos: {e}")
    #         raise  # Relanza la excepción para que pytest lo detecte como un
    # # app.run()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
