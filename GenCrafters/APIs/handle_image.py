from flask import Flask, request, jsonify
import base64
import os
from io import BytesIO
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_image():
    data = request.json
    if 'image' not in data:
        return jsonify({'error': 'No image data provided'}), 400

    image_data = data['image']
    if image_data.startswith('data:image'):
        header, image_data = image_data.split(',', 1)

    try:
        decoded_image = base64.b64decode(image_data)
        image = Image.open(BytesIO(decoded_image))

        # Save the image under two different filenames
        image_path_llm = os.path.join('.', 'uploaded_image_llm.png')
        image_path_ui = os.path.join('.', 'uploaded_image_ui.png')
        image.save(image_path_llm)
        image.save(image_path_ui)

        return jsonify({'message': 'Image uploaded successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_image(image_path):
    if not os.path.exists(image_path):
        return jsonify({'image': 0})

    try:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        os.remove(image_path)
        return jsonify({'image': encoded_image})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_image_llm', methods=['GET'])
def get_image_llm():
    image_path = os.path.join('.', 'uploaded_image_llm.png')
    return get_image(image_path)

@app.route('/get_image_ui', methods=['GET'])
def get_image_ui():
    image_path = os.path.join('.', 'uploaded_image_ui.png')
    return get_image(image_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)

