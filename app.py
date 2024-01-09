import io
import requests
from flask import Flask, request, Response, jsonify
from rembg import remove
from flask_cors import CORS, cross_origin
import base64

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def index():
    ok_data = {"ok": True}
    response = jsonify(ok_data)
    response.status_code = 200

    return response

@app.route('/removebg', methods=['POST'])
@cross_origin()
def process_images():
    if (request.json['imageURL'] == None):
        return "No image URL provided", 400
    
    url = request.json['imageURL']

    # Download the image from the URL
    response = requests.get(url)
    image_data = response.content

    input_file_path = "input_image.png"

    # Save the image to a file

    with open(input_file_path, "wb") as input_file:
        input_file.write(image_data)
        input_file.close()

    with open(input_file_path, "rb") as image_file:
        file = remove(image_file.read())

    base64_string = base64.b64encode(file).decode('utf-8')
    return jsonify({'image_data': base64_string})
    
if __name__ == '__main__':
    app.run(debug=True)