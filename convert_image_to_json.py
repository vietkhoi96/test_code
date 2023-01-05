from PIL import Image
from pytesseract import pytesseract
import json
path_to_image = '/home/khoinv/Downloads/excel.jpg'
img = Image.open(path_to_image)
text = pytesseract.image_to_string(img)
for i in 
with open('text.txt', 'w') as f:
    f.write(text)
file = '/home/khoinv/text.txt'
dict = {}
