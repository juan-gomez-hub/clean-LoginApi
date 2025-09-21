from flask import Blueprint, request, jsonify
from app.infrastructure.repository.userRepository import UserRepository
from app.interface.controllers.user_controller import UserController
from app.use_cases.user import LoginUserUseCase, createUserUseCase
from app.infrastructure.middleware.auth_middleware import login_required

user_bp = Blueprint('user', __name__)

repo = UserRepository()
create_use_case = createUserUseCase(repo)
login_use_case = LoginUserUseCase(repo)
user_controller = UserController(create_use_case, login_use_case)

@user_bp.route('/create-user', methods=['POST'])
def get_users():
    return user_controller.create_user()
    

@user_bp.route('/login',methods=['POST'])
@login_required
def login():
    return user_controller.login()