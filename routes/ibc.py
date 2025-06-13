from flask import Blueprint, render_template
from datetime import datetime

ibc_app = Blueprint('IBC', __name__)

@ibc_app.route('/IBC')
def ibc_form():    
    return render_template("IBC.html", year=datetime.now().year)
