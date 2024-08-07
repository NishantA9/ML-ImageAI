
from imageai.Classification import ImageClassification
import os

# Set execution path
exec_path = os.getcwd()

# Initialize ImageClassification object
prediction = ImageClassification()

# Set model type and path
prediction.setModelTypeAsMobileNetV2()
model_path = os.path.join(exec_path, 'mobilenet_v2-b0353104.pth')
if not os.path.isfile(model_path):
    raise ValueError(f"The path '{model_path}' isn't a valid file. Ensure you specify the path to a valid trained model file.")
prediction.setModelPath(model_path)

# Load the model
prediction.loadModel()

# Classify an image and print the results
image_path = os.path.join(exec_path, 'giraffe.jpg')
if not os.path.isfile(image_path):
    raise ValueError(f"The path '{image_path}' isn't a valid file. Ensure you specify the path to a valid image file.")

predictions, probabilities = prediction.classifyImage(image_path, result_count=5)
for eachPred, eachProb in zip(predictions, probabilities):
    print(f'{eachPred} : {eachProb}')
