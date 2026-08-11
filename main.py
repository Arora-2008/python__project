from flask import Flask, jsonify, send_from_directory,request

app = Flask(__name__)



# #home
@app.route("/")
def index():
    return send_from_directory('.','index.html')


# #chat
# @app.route("/chat")
# def chat():
#     return "chat"




# # image
# @app.route("/image")
# def image():
#     return "image"



# # video
# @app.route("/video")
# def video():
#     return "video"


# @app.after_request
# def add_cors_headers(response):
#     response.headers['Access-Control-Allow-Origin']='*'
#     response.headers['Access-Control-Allow-Methods']='GET,POST,OPTIONS'
#     response.headers['Access-Control-Allow-Headers']='Content-Type'
#     return response




# @app.route('/api/data',methods=['GET'])
# def get_data():
#     return jsonify({"message":"Hello!"})



@app.route('/api/sum',methods=['POST'])
def sum_numbers():
    if not request.is_json:
        return jsonify({"error": "Expected JSON body with 'a' and 'b'"}),400
    data=request.get_json()
    try:
        a = data.get('a')
        b = data.get('b')
        # Accept numbers or numeric strings  
        a = float(a)
        b = float(b) 
    except Exception:
        return jsonify({"error":"Invalid numbers provided"}),400
    result = a+b
    return jsonify({"sum":result})


    
if __name__ == "__main__":
    app.run(debug=True)








