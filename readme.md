# Image Classification with ImageAI and MobileNetV2

This project demonstrates how to use the ImageAI library with the MobileNetV2 model for image classification. It involves setting up the environment, loading the pre-trained MobileNetV2 model, and classifying an image.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- pip (Python package installer)

Install the necessary Python packages:
```bash
pip install imageai tensorflow numpy

# Project Structure

.
├── classify_image.py
├── giraffe.jpg
├── mobilenet_v2-b0353104.pth
└── README.md

# Usage and Script Details

Clone the repository (if applicable) or download the project files to your local machine.
Ensure the pre-trained MobileNetV2 model file is in the project directory. You can download it from the official sources if not present.
Run the script to classify an image:

Here's a brief overview of what the classify_image.py script does:

Sets up the execution path.
Initializes the ImageClassification object.
Configures the model type and path.
Loads the model.
Classifies a given image and prints the top 5 predictions along with their probabilities.

Notes
Make sure the mobilenet_v2-b0353104.pth file and the image you want to classify are in the same directory as the script.
Replace giraffe.jpg with your desired image file for classification.

Search for following documentation:
ImageAI Documentation
MobileNetV2 Model

Made by Nishant Acharekar, under Course of Complete Python Developer 2024 by ZTM on Udemy