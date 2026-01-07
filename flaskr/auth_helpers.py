from functools import wraps
from flask import session, redirect, url_for, abort


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


def role_required(*roles):
    def decorator(view):
        @wraps(view)
        def wrapped_view(**kwargs):
            if 'user_role' not in session:
                return abort(403)

            if session['user_role'] not in roles:
                return abort(403)

            return view(**kwargs)
        return wrapped_view
    return decorator
