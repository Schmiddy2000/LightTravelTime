# Imports
import numpy as np
from matplotlib import image as mpimg
from matplotlib import pyplot as plt

from typing import Optional


def get_amplitude(image_index: int, show_img: bool = False) -> Optional[int]:
    img = mpimg.imread(f'Oscilloscope data/DS1Z_QuickPrint{image_index}.bmp')

    orange = [248, 128, 0, 255]
    black = [0, 0, 0, 255]
    gray = [48, 48, 48, 255]

    disregarded_colors = [orange, black, gray]

    # Yellow means only RG-values and Blue means only

    left_start = 84
    top_start = 39
    right_stop = 683
    bottom_stop = 396

    start_row = 0
    stop_row = 0
    did_set_start_row = False
    no_disregard_this_row = True
    found_amplitude = False

    for i in range(top_start, bottom_stop):
        no_disregard_this_row = True

        for j in range(left_start, right_stop):
            if list(img[i][j]) not in disregarded_colors:
                no_disregard_this_row = False

                if not did_set_start_row:
                    start_row = i
                    did_set_start_row = True

            if j == right_stop - 1 and no_disregard_this_row and did_set_start_row:
                stop_row = i
                found_amplitude = True

                print(f'Start row: {start_row}, Stop row: {stop_row} --> Amplitude: {stop_row - start_row}')

        if found_amplitude:
            break

    # Display the image
    if show_img:
        plt.imshow(img)
        plt.show()

    if found_amplitude:
        return stop_row - start_row
    else:
        print("Couldn't find an amplitude in this image")

        return None


# print(get_amplitude(1, True))


# ToDo's:
# - Define the positions for the various components that should then be read using OCR
def get_voltage_dimension(image_index: int) -> None:
    img = mpimg.imread(f'Oscilloscope data/DS1Z_QuickPrint{image_index}.bmp')
    dim = np.shape(img)
    cropped_img = img[dim[0] - 100:dim[0] - 1]#[:, 100:200]

    plt.imshow(cropped_img)
    plt.show()

    return None


get_voltage_dimension(1)
