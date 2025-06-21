from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from werkzeug.security import check_password_hash
from models import db, User
from Service.service import emailService
import random
import string

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# class for Login & OTP
class authController:
    def __init__(self):
        self.email_service = emailService()

    def generate_OTP(self, length=6):
        return ''.join(random.choices(string.digits, k=length))
    
    def verify_credentials(self, email, password):
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            return user
        return None
    
    def send_otp(self, to_email, otp_code):
        subject = "Your OTP Code"
        body = f"Hi, Here is your OTP code: {otp_code}"
        self.email_service.send_email(to_email, subject, body)

auth_controller = authController()

# Route: Login
@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = auth_controller.verify_credentials(email, password)

        if user:
            otp_code = auth_controller.generate_OTP()
            session['otp'] = otp_code
            session['email'] = user.email
            session['name'] = user.name
            auth_controller.send_otp(user.email, otp_code)

            flash("OTP have sent to your Email", "info")
            return redirect(url_for("auth.verify_otp"))
        
        else:
            flash("Invalid Email and Password", "danger")
    
    return render_template('login.html', hide_nav=True)

# Route: verify OTP
@auth_bp.route('/verify_otp', methods=["GET","POST"])
def verify_OTP():
    if request.method == "POST":
        entered_OTP = request.form.get('otp')

        if entered_OTP == session.get('otp'):
            session["username"] == session.get('name')
            flash("Login Successful", "success")
            return redirect(url_for("arrival_check.arrival_check"))
        else:
            flash("OTP is Incorrect", "danger")

    return render_template("Verify_OTP.html", hide_nav=True)

@auth_bp.route('/logout')
def logout():
    
    session.clear()
    return redirect(url_for('auth.login'))
