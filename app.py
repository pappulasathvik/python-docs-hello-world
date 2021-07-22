from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello,jhansi,Take the rest and do someting"
