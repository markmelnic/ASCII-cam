import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw

SHRT_CHAR_LIST = "@%#*+=-:. " # short
LONG_CHAR_LIST = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. " # long

BG_CODE = 255 # white
BG_CODE = 0 # black

def aschier(img):
    SCALE = 1
    NUM_COLS_RESOLUTION = 200

    font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size=10 * SCALE)
    num_chars = len(LONG_CHAR_LIST)

    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = image.shape
    cell_width = width / NUM_COLS_RESOLUTION
    cell_height = 2 * cell_width
    num_rows = int(height / cell_height)
    if NUM_COLS_RESOLUTION > width or num_rows > height:
        print("too many rows or columns")
        # default width and height
        cell_width = 6
        cell_height = 12

        NUM_COLS_RESOLUTION = int(width / cell_width)
        num_rows = int(height / cell_height)
    char_width, char_height = font.getsize("A")

    out_width = char_width * NUM_COLS_RESOLUTION
    out_height = 2 * char_height * num_rows
    out_image = Image.new("L", (out_width, out_height), BG_CODE)
    draw = ImageDraw.Draw(out_image)
    for i in range(num_rows):
        line = "".join([
            LONG_CHAR_LIST[
                min(int(np.mean(
                    image[
                        int(i * cell_height):min(int((i + 1) * cell_height), height),
                        int(j * cell_width):min(int((j + 1) * cell_width), width)]
                    ) * num_chars / 255), num_chars - 1)]
            for j in
                range(NUM_COLS_RESOLUTION)]) + "\n"
        draw.text((0, i * char_height), line, fill=255 - BG_CODE, font=font)

    return np.asarray(out_image.crop(out_image.getbbox()))
