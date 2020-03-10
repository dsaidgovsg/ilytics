from flask_cors import CORS
from flask import Flask, jsonify, request
import base64
import darknet
import os
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)
stats = []

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({'data': 'pong!'})

@app.route('/upload', methods=['POST'])
def uploadFile():
    file = request.files['file']
    file.save("./test.jpg")
    stats = darknet.performDetect(imagePath="./test.jpg")
    with open("result.jpg","rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        base64_string = encoded_string.decode('utf-8')
    return jsonify(img=base64_string, stat=stats)



if __name__ == '__main__':
   # predict()  
   app.run(host='0.0.0.0', port=8080)
