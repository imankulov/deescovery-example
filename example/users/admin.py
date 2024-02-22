from flask import Blueprint, url_for


admin = Blueprint('users', __name__, url_prefix="/users")


@admin.route('/support')
def support():
    return url_for('admin.users.support')
