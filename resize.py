from PIL import Image
import os

for file in os.listdir("images"):
    if file.endswith(".jpg"):
        img = Image.open(f"images/{file}")
        img = img.resize((800, 800))
        img.save(f"images/resized_{file}")
