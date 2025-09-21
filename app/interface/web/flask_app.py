from flask import Flask, jsonify
from app.interface.web.routers.user_route import user_bp
from app.infrastructure.db.db_connect import DatabaseConnection


def create_app(testing=False):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    if not testing:
        db = DatabaseConnection(False)
    else:
        db = DatabaseConnection(True)
    with db.get_connection() as conn:
        print("Database connected:", conn is not None)
        db.execute_schema("sql/schema.sql")

    @app.route('/status', methods=['GET'])
    def status():
        return jsonify({"status": "ok"}), 200
    app.register_blueprint(user_bp)

    return app

# if __name__=="__main__":
    # app = create_app()
    # app.run
