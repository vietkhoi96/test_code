from PIL import Image
from pytesseract import pytesseract
import json
a =[]
path_to_image = '/home/khoinv/Downloads/excel.jpg'
img = Image.open(path_to_image)
text = pytesseract.image_to_string(img)
with open('text.txt', 'w') as f:
    f.write(text)
print(text)
