from flask import Flask, render_template
from datetime import datetime
from routes.arrival_check import arrival_check_app
from routes.storage_maintenance_list import storage_maintenance_list_app
from routes.pre_delivery_list import pre_delivery_app
from routes.ibc import ibc_app
from routes.auth import auth_bp
from routes.storage_maintenance_list import storage_maintenance_list_app

app = Flask(__name__)
app.secret_key = 'secret-key'

# register semua blueprint
app.register_blueprint(arrival_check_app)
app.register_blueprint(storage_maintenance_list_app)
app.register_blueprint(pre_delivery_app)
app.register_blueprint(ibc_app)
app.register_blueprint(auth_bp)

@app.route('/')
def base():
    return render_template("Base.html", year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True)
