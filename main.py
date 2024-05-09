from flask import Flask
from routes.home import homeroute
from routes.clients import clientroute

app = Flask(__name__)

app.register_blueprint(homeroute)
app.register_blueprint(clientroute, url_prefix="/clients")

app.run(debug=True)