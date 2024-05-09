from flask import Blueprint, render_template

homeroute = Blueprint("home" , __name__)

@homeroute.route('/')
def home():
    return render_template("index.html")