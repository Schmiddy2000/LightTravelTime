# Imports
import numpy as np
from matplotlib import pyplot as plt

# General data
box_height_in_pixels = 45

# Information about some images
# - filename_11 / 12 showed artifacts and some dips were lower than others
# - filename_15 and higher often seem to have multilayered and shifted signals


# Data day 1
# Found issue: There is no measurement at '17'. The lab notes go ..., 16, 18, ...
frequencies = np.array([172, 250, 500, 755, 1000, 1503, 1980, 2003, 3022, 3504, 4004, 4965, 5990, 6995, 8023, 8992,
                        10070, 11071, 12040, 13010, 14100, 14835, 15883, 16800, 17620, 19290, 19840, 20240])
frequency_errors = np.array([5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 3, 10, 10, 10, 10, 10])

# Here, the first value is chosen plausibly because the device displayed '****'
# For 1kHz, only the first two digits after the decimal point were displayed, for 10kHz only the first decimal point
oscilloscope_frequencies = np.array([172, 256, 505, 757, 990, 1510, 1980, 2470, 3010, 3520, 4030, 5000, 5950, 6990,
                                     8060, 9090, 10100, 11000, 12500, 12900, 14100, 14300, 15800, 16500, 17800, 19100,
                                     21400, 20800])

amplitude_pixel_heights = np.array([181, 184, 175, 162, 142, 117, 234, 194, 167, 147, 130, 108, 85, 156, 140, 126,
                                    113, 105, 99, 90, 90, 54, 52, 36, 34, 37, 36, 35])

# What exactly is this?
voltage_dimensions = -1 * np.array([1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.14, 1.14, 1.14, 1.14, 1.14, 1.14, 1.14,
                                    0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.94, 0.94, 0.56, 0.56, 0.56, 0.56, 0.56,
                                    0.56, 0.56])

# In mV
chosen_voltage = np.array([500, 500, 500, 500, 500, 500, 200, 200, 200, 200, 200, 200, 200, 100, 100, 100, 100, 100,
                           100, 100, 100, 100, 100, 100, 100, 100, 100, 100])

print(amplitude_pixel_heights[0] / box_height_in_pixels)

print(len(oscilloscope_frequencies), len(amplitude_pixel_heights), len(voltage_dimensions), len(chosen_voltage))


plt.figure(figsize=(12, 5))
plt.title('Chopper frequency against voltage amplitude')
plt.xlabel('Chopper frequency in [Hz]')
plt.ylabel('Voltage amplitude in [mV]')

plt.scatter(frequencies, chosen_voltage * amplitude_pixel_heights / box_height_in_pixels)
plt.show()
