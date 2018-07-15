from datetime import datetime
from flask import Flask
from application import app

@app.route('/')
def home():
    return "Everything Fine", 200

@app.route('/notfound')
def notfound():
    return "Page Not Found", 404