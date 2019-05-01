from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello There , This is Web based application to create COntrol-M xmls!"
