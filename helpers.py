import math


def convert_rgb_to_brightness(rgb_tuple: tuple[int, int, int]) -> int:
    # Formula: Brightness = (R + G + B) / 3
    brightness = (rgb_tuple[0] + rgb_tuple[1] + rgb_tuple[2]) // 3
    return brightness


def brightness_to_ascii(brightness: int) -> str:
    ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    factor = 256 / len(ascii_chars)
    idx = math.floor(brightness / factor)
    return ascii_chars[idx]


MATRIX_GREEN = "\033[32m"
RESET = "\033[0m"


def print_matrix(matrix):
    print(MATRIX_GREEN)
    for row in matrix:
        for char in row:
            print(char * 3, end="")
        print("")
    print(RESET)
