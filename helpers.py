import math
from rich.console import Console

console = Console()


def convert_rgb_to_brightness(rgb_tuple: tuple[int, int, int], algorithm="average") -> int:
    red = rgb_tuple[0]
    green = rgb_tuple[1]
    blue = rgb_tuple[2]

    brightness = None

    if algorithm == "average":
        brightness = (red + green + blue) // 3
    elif algorithm == "min_max":
        brightness = (max(red, green, blue) + min(red, green, blue)) // 2
    else:
        brightness = math.floor(0.21 * red + 0.72 * green + 0.07 * blue)

    return brightness


def brightness_to_ascii(brightness: int) -> str:
    ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    factor = 256 / len(ascii_chars)
    idx = math.floor(brightness / factor)
    return ascii_chars[idx]


def print_ascii_image(matrix):
    ascii_string = ""
    for row in matrix:
        for char in row:
            ascii_string += char * 3
        ascii_string += "\n"

    console.out(ascii_string, style="#003B00 on #000000", highlight=False)
