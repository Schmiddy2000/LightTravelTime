# Imports
import matplotlib.image as mpimg


def get_amplitude(image_index: int):
    img = mpimg.imread(f'Oscilloscope data/DS1Z_QuickPrint{image_index}.bmp')

    orange = [248, 128, 0, 255]
    black = [0, 0, 0, 255]
    gray = [48, 48, 48, 255]

    disregarded_colors = [orange, black, gray]

    left_start = 84
    top_start = 39
    right_stop = 683
    bottom_stop = 396

    start_row = 0
    stop_row = 0
    did_set_start_row = False
    no_disregard_this_row = True

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

                print(f'Start row: {start_row}, Stop row: {stop_row} --> Amplitude: {stop_row - start_row}')

                return stop_row - start_row

    # Display the image
    # plt.imshow(img)
    # plt.show()


get_amplitude(1)
