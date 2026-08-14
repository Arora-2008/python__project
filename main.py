from flask import Flask
from route import route

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(route)

if __name__ == "__main__":
    print("🚀 Starting Server on http://127.0.0.1:5000")
    print("  - Text Chat:  http://127.0.0.1:5000/text")
    print("  - Photo Chat: http://127.0.0.1:5000/photo")
    print("  - Video Chat: http://127.0.0.1:5000/video")
    print("  - Audio Chat: http://127.0.0.1:5000/audio")
    app.run(debug=True, port=5000)


