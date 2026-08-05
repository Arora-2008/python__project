from flask import Flask as f

app = f(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
