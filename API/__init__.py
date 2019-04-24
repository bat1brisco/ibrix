from flask import Flask

app = Flask(__name__)

from API.Userroutes.userroutes import mod

app.register_blueprint(Userroutes.userroutes.mod)