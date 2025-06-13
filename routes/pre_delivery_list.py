from flask import Blueprint, render_template
from datetime import datetime

pre_delivery_app = Blueprint('pre_delivery_list', __name__)

@pre_delivery_app.route('/pre_delivery_list')
def pre_delivery_list():    
    return render_template("Pre_delivery_list.html", year=datetime.now().year)
