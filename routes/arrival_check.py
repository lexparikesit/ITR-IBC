from flask import Blueprint, render_template
from datetime import datetime

arrival_check_app = Blueprint('arrival_check', __name__)

@arrival_check_app.route('/arrival_check')
def arrival_check():    
    return render_template("Arrival_check.html", year=datetime.now().year)
