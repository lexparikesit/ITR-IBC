from flask import Blueprint, render_template, session, redirect, url_for

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    
    session.clear()
    return redirect(url_for('auth.login'))
