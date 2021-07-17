from flask import Flask

app = Flask(__name__)

@app.route("/:<name>")
def hello_name(name):
    return "<h1>Hello, {name}</h1>"