from PIL import Image
import numpy as np
import helpers

# Load image
img = Image.open("test/test.jpg")
img = img.resize((320, 240))

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
