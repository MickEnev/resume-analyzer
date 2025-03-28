from flask import Flask
import time
import proessor

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Index</p>"

@app.route("/time")
def get_time():
    return {'time': time.time()}

@app.rooute("/skills")
def get_skills():
    return