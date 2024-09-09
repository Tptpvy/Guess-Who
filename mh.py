import random
import math
from PIL import Image
import os

mhPath = ".../monhun/" # your path
x = 24
mhArray = []
while len(mhArray) < x:
    random_index = random.randint(0, 148)
    if random_index not in mhArray:
        mhArray.append(random_index)
height = 200
width = 200
new_image = Image.new('RGB', (width * 6, height * 4))
for i in range(len(mhArray)):
    file_path = os.path.join(mhPath, f"{mhArray[i]}.jpg")
    if not os.path.exists(file_path):
        file_path = os.path.join(mhPath, f"{mhArray[i]}.png")

    if os.path.exists(file_path):
        image = Image.open(file_path)
        new_image.paste(image, (width * (i % 6), height * math.floor(i / 6)))

new_image.show()
