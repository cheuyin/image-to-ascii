from PIL import Image
import numpy as np
import helpers
import argparse

parser = argparse.ArgumentParser(
    description="A program that converts an image to ASCII")
parser.add_argument("filename", help="The path of the image to convert")

args = parser.parse_args()

# Load image
img = Image.open(args.filename)
img = img.resize((160, 120))

img_matrix = np.array(img, dtype=np.int16)
height = img_matrix.shape[0]
width = img_matrix.shape[1]

# Create brightness matrix
brightness_matrix = np.array([[0] * width] * height, dtype=np.uint8)

for x in range(width):
    for y in range(height):
        brightness_matrix[y][x] = helpers.convert_rgb_to_brightness(
            img_matrix[y][x])

# Create ASCII matrix
ascii_matrix = np.array([[None] * width] * height)
for x in range(width):
    for y in range(height):
        ascii_matrix[y][x] = helpers.brightness_to_ascii(
            brightness_matrix[y][x])

helpers.print_matrix(ascii_matrix)
