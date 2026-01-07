from flask import Blueprint
from flaskr.auth_helpers import login_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/protected')
@login_required
def protected():
    return "Protected route"
