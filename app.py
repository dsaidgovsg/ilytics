from flask_cors import CORS
from flask import Flask, jsonify, request
import base64
import darknet
import os
import autocrop

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)
stats = []


@app.route("/")
def helloWorld():
    """
    Root route

    Returns:
        String -- Return a valid string
    """
    return "Hello, cross-origin-world!"


@app.route('/ping', methods=['GET'])
def pingPong():
    """
    Ping route for sanity check

    Returns:
        JSON Dictionary -- Return a valid key value pair
    """
    return jsonify({'data': 'pong!'})


@app.route('/upload', methods=['POST'])
def uploadFile():
    """
    REST API endpoint for image inference

    Returns:
        JSON Dictionary -- Return a dictionary containing image in base64 format and statistics of the counts and classification of rotifers
    """
    file = request.files['file']
    auto_crop = int(request.form['auto_crop'])
    file.save("./test.jpg")

    if auto_crop == 1:
        autocrop.autocrop("./test.jpg")

    stats = darknet.performDetect(imagePath="./test.jpg", configPath="./yolo-obj.cfg",
                                  weightPath="./backup/yolo-obj_best.weights", metaPath="./data/obj.data")
    with open("result.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        base64_string = encoded_string.decode('utf-8')
    return jsonify(img=base64_string, stat=stats)


if __name__ == '__main__':
    # predict()
    app.run(host='0.0.0.0', port=8888)
