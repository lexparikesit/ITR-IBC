from flask import Blueprint, render_template
from datetime import datetime

storage_maintenance_list_app = Blueprint('storage_maintenance_bp', __name__)

@storage_maintenance_list_app.route('/storage_maintenance_list')
def storage_maintenance_list():    
    return render_template("Storage_maintenance_list.html", year=datetime.now().year)
