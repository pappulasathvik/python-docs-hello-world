from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello,Lakshmikanth, What are you doing and learn datascience"
