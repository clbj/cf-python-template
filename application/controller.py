from datetime import datetime
from flask import Flask, render_template
from application import app

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/notfound')
def notfound():
    return "Page Not Found", 404