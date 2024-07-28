# Professional Headshot Generator

This project is a web application that uses AI to generate professional headshots from user-uploaded images. It leverages the Stability AI API to transform regular photos into high-quality, studio-like professional headshots.

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup and Installation](#setup-and-installation)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [API Reference](#api-reference)
7. [Contributing](#contributing)
8. [License](#license)

## Features

- User-friendly interface for image upload
- AI-powered image transformation
- Responsive design for various devices
- Real-time feedback and loading indicators

## Technologies Used

- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- AI API: Stability AI
- Image Processing: Pillow (Python Imaging Library)

## Setup and Installation

1. Clone the repository: git clone https://github.com/yourusername/professional-headshot-generator.git
                        cd professional-headshot-generator

2. Create a virtual environment and activate it:python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

3. Install the required dependencies: pip install flask pillow requests

4. Set up your Stability AI API key:
- Sign up for an account at [Stability AI](https://stability.ai/)
- Obtain your API key
- Replace `'your-api-key-here'` in `app.py` with your actual API key

5. Run the application: python app.py

6. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Click on "Choose Image" to select a photo from your device.
2. Click "Generate Headshot" to start the AI transformation process.
3. Wait for the process to complete. A loading spinner will indicate progress.
4. Once complete, the generated professional headshot will be displayed.

## How It Works

1. **Image Upload**: The user selects an image file through the web interface.
2. **Image Preprocessing**: The uploaded image is resized to 1024x1024 pixels to meet the API requirements.
3. **API Request**: The preprocessed image is sent to the Stability AI API along with specific parameters for headshot generation.
4. **AI Processing**: The Stability AI model processes the image, applying transformations to create a professional headshot.
5. **Result Display**: The generated headshot is returned and displayed to the user.

## API Reference

This project uses the Stability AI API. For more information, visit [Stability AI API Documentation](https://stability.ai/documentation).

Key API parameters used:
- `text_prompts`: Specifies the style of the headshot (e.g., "professional headshot, high quality, studio lighting, neutral background")
- `init_image_mode`: Set to "IMAGE_STRENGTH" for image-to-image transformation
- `image_strength`: Determines how much of the original image to preserve (set to 0.6)
- `cfg_scale`: Controls the strength of the prompt guidance (set to 8.0)
- `steps`: Number of diffusion steps (set to 50)

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

