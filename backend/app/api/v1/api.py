from flask import Blueprint

from app.api.v1.routes.auth import auth_bp
from app.api.v1.routes.user import user_bp
from app.api.v1.routes.user_pokemon import user_pokemon_bp

api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api_v1_bp.register_blueprint(user_bp)
api_v1_bp.register_blueprint(auth_bp)
api_v1_bp.register_blueprint(user_pokemon_bp)
