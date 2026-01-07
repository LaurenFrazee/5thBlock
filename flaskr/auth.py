from flask import Blueprint, request, session

from flaskr.models import Parent, Student, Teacher

auth_bp = Blueprint(
    'auth',
    __name__,
    url_prefix='/auth'
)


auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = (
            Teacher.query.filter_by(email=email).first() or
            Parent.query.filter_by(email=email).first() or
            Student.query.filter_by(username=email).first()
        )

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_role'] = user.__class__.__name__
            return "Logged in successfully"
        
        return "Invalid credentials", 401
    
    return 'Login page place holder'
        
@auth_bp.route('/logout')
def logout():
    session.clear()
    return "Logged out successfully"