from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello_world():
    return "<input type='text' placeholder='Enter your name' />"
if __name__ == "__main__ ":
    app.run()