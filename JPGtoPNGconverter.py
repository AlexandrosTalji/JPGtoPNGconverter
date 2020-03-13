import sys
import os
from PIL import Image

# The images folder where I want to take the JPG images from
path = sys.argv[1]
# The images folder where I want to place the PNG images to
directory = sys.argv[2]

if not os.path.exists(directory):  # If the new directory doesn't exist
    os.makedirs(directory)  # Create one (new)

# To access the JPG images in the folder one by one
for filename in os.listdir(path):
    # The splitext will give a tuple of the files names and extentions. We want only the name so we move the extentions .jpg
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')

# To run this program, type in the terminal # python3 JPGtoPNGconverter.py <JPGimagesFolder>/ new/
