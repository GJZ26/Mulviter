import shutil
import sys
import os

pixeld = [
    u"\u2591",
    u"\u2592",
    u"\u2593",
    u"\u2588",
]


def get_terminal_size():
    width, height = shutil.get_terminal_size()
    return (int(width/2), height)


def to_string_image(image):
    output = []
    max_val, min_val = image.max(), image.min()
    step = (max_val - min_val) / 4
    for image_row in image:
        row = ""
        for pixel in image_row:
            if pixel < min_val + step:
                light_value = pixeld[0]
            elif pixel < min_val + 2 * step:
                light_value = pixeld[1]
            elif pixel < min_val + 3 * step:
                light_value = pixeld[2]
            else:
                light_value = pixeld[3]
            row += light_value * 2
        output.append(row)
    return output


def render(message):
    sys.stdout.write("\033[H")
    sys.stdout.flush()
    sys.stdout.write("\n".join(message))
    sys.stdout.flush()


def clear():
    os.system("cls" if os.name == "nt" else "clear")
