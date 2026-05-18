# Create and Art with Neural style transfer on given image using deep learning

import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# Function to load image from URL
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((256, 256))
    img = np.array(img) / 255.0
    img = img[np.newaxis, :]
    return tf.constant(img, dtype=tf.float32)

# Content image (given image URL)
content_url = "https://th.bing.com/th/id/OIP.yvmowZLNvdK20X76vAsSYAHaE8?o=7rm=3&rs=1&pid=ImgDetMain&o=7&rm=3"

# Style image URL
style_url = "https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Starry_Night.jpg"

# Load images
content_image = load_image(content_url)
style_image = load_image(style_url)

# Load pre-trained model
model = hub.load(
'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
)

# Apply Neural Style Transfer
stylized_image = model(content_image, style_image)[0]

# Show Output
plt.imshow(stylized_image[0])
plt.axis('off')
plt.title("Neural Style Transfer Output")
plt.show()



#pip install tensorflow tensorflow_hub matplotlib pillow requests

# 1. Problem Statement
# Apply Neural Style Transfer (NST) to generate artistic images.

# 👉 Goal:
# Take Content Image (your photo)
# Take Style Image (painting like Van Gogh)
# Combine both to create a stylized output image
# 👉 Example:
# Content → Your building/face image
# Style → Painting style
# Output → Your image in painting style

# 🧠 2. Concept (Simple Explanation)
# Neural Style Transfer uses a deep learning model like VGG19 to:
# Preserve content (structure of image)
# Apply style (colors, textures)
# 👉 It works using:
# Content Loss
# Style Loss
# Total Loss

# 💻 3. Python Code (Using PyTorch)

# 📁 Create file:
# neural_style_transfer.py

# 📌 Install libraries:
# pip install torch torchvision pillow matplotlib

# . How to Run in VS Code
# Step 1: Open VS Code
# Step 2: Create file:
# neural_style_transfer.py
# Step 3: Add images in same folder:
# content.jpg
# style.jpg
# Step 4: Open terminal:
# Terminal → New Terminal
# Step 5: Run:
# python neural_style_transfer.py
# 🖼️ 5. Output Explanation
# Console Output:
# Starting Style Transfer...
# Step 0, Loss: 12.3456
# Step 50, Loss: 5.2341
# Step 100, Loss: 2.1123
# Step 150, Loss: 1.2345
# Style Transfer Completed!

# 👉 Loss decreases → model improving

# Final Output:
# A new image appears
# Looks like:
# Same structure as content image
# Style applied from style image
# 🔍 6. Code Explanation
# Load Image
# load_image("content.jpg")

# 👉 Converts image to tensor

# Model
# vgg19(pretrained=True)

# 👉 Pretrained CNN used for feature extraction

# Output Image
# output = content.clone()

# 👉 Start from content image

# Loss Calculation
# content_loss + style_loss

# 👉 Content Loss → keeps structure
# 👉 Style Loss → adds artistic texture

# Optimization
# optimizer.step()

# 👉 Updates image pixels

# 🎤 7. Viva Questions

# Q1. What is Neural Style Transfer?
# 👉 A technique to combine content and style of two images.

# Q2. Which model is used?
# 👉 VGG19 (pretrained CNN)

# Q3. What is content loss?
# 👉 Difference in structure between images.

# Q4. What is style loss?
# 👉 Difference in texture and colors.

# Q5. What is optimizer used?
# 👉 Adam optimizer

# Q6. Why use pretrained model?
# 👉 It already learned image features.

# Q7. What is output of NST?
# 👉 Stylized artistic image.

# Q8. Can NST be used in real life?
# 👉 Yes, in apps, design, filters, AI art.

# 💡 Final Tip (For Exam)

# 👉 Always write:

# Content image + Style image
# VGG19 model
# Loss = Content + Style