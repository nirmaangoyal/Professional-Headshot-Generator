import os
from flask import Flask, request, send_file, render_template, jsonify
import requests
from PIL import Image
import io

app = Flask(__name__, static_folder='templates/static')


# Set your Stability API key
STABILITY_API_KEY = 'Your_key'  # Replace with your actual API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_headshot', methods=['POST'])
def generate_headshot():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    init_image = Image.open(file.stream)

    # Resize the image to 1024x1024
    init_image = init_image.resize((1024, 1024), Image.LANCZOS)

    # Save the resized image to a temporary file
    temp_file = io.BytesIO()
    init_image.save(temp_file, format='PNG')
    temp_file.seek(0)

    headers = {
        'Authorization': f'Bearer {STABILITY_API_KEY}',
        'Accept': 'image/png'
    }

    files = {
        'init_image': ('image.png', temp_file, 'image/png')
    }

    data = {
        'text_prompts[0][text]': 'professional headshot, high quality, studio lighting, business suit, crisp details, office background, minimal facial alterations',
        'text_prompts[0][weight]': 0.9,
        'init_image_mode': 'IMAGE_STRENGTH',
        'image_strength': 0.65,
        'cfg_scale': 15.0,
        'samples': 1,
        'steps': 50,
        'style_preset': 'photographic'
    }

    response = requests.post(
        'https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/image-to-image',
        headers=headers,
        files=files,
        data=data
    )

    if response.status_code == 200:
        return send_file(io.BytesIO(response.content), mimetype='image/png')
    else:
        error_message = response.json().get('message', 'Unknown error')
        return jsonify({'error': error_message}), response.status_code

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
