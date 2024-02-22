from flask import Blueprint, url_for


api = Blueprint('users', __name__, url_prefix="/users")


@api.route('/support')
def support():
    return url_for('api.users.support')
