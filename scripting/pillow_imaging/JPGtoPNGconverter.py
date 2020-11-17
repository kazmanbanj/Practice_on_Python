import sys
import os
from PIL import Image

image_folder = sys.argv[1]  # represents argument 1 when called in the terminal
output_folder = sys.argv[2]  # represents argument 2 when called in the terminal

# print(image_folder, output_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done')


# run this to create a new folder and move the files in images to the new folder
# .\JPGtoPNGconverter.py images/ new/