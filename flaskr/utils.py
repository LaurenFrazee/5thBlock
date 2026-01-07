from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to access this page.")
            return redirect(url_for('auth.login'))
        return view(*args, **kwargs)
    return wrapped_view

def teacher_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if session.get('role') != 'teacher':
            flash("Unauthorized access.")
            return redirect(url_for('auth.login'))
        return view(*args, **kwargs)
    return wrapped_view

def student_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if session.get('role') != 'student':
            flash("Unauthorized access.")
            return redirect(url_for('auth.login'))
        return view(*args, **kwargs)
    return wrapped_view

def parent_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if session.get('role') != 'parent':
            flash("Unauthorized access.")
            return redirect(url_for('auth.login'))
        return wrapped_view(*args, **kwargs)
    return wrapped_view
