# Imports
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

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
oscilloscope_frequencies_2 = np.array([65, 1330, 1420, 1510, 1620, 1680, 1820, 1940, 19080, 2140, 2290, 2450,
                                       2750, 2910, 3120, 3250, 4490, 5590, 6100, 6210,6330, 6450, 6710])


amplitude_pixel_heights = np.array([181, 184, 175, 162, 142, 117, 234, 194, 167, 147, 130, 108, 85, 156, 140, 126,
                                    113, 105, 99, 90, 90, 54, 52, 36, 34, 37, 36, 35])

amplitude_pixel_heights_2 = np.array([288, 207, 196, 193, 200, 180, 176, 171, 164, 164, 156, 152, 140, 135, 129,
                                      124, 97, 86, 63, 78, 77, 76, 76])



# Using thinner, starting at filename_8, distinct voltage amplitude lines (higher errors on the pixels here, since
# the exact highest and lowest points are rather hard to infer due to their overlap)
amplitude_conservative_pixel_heights = np.array([181, 184, 175, 162, 142, 117, 223, 189, 156, 135, 115, 100, 86, 136,
                                                 122, 109, 97, 88, 83, 79, 70, 43, 41, 36, 34, 37, 35, 36])

# What exactly is this?
voltage_dimensions = -1 * np.array([1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.14, 1.14, 1.14, 1.14, 1.14, 1.14, 1.14,
                                    0.968, 0.968, 0.968, 0.968, 0.968, 0.968, 0.94, 0.94, 0.56, 0.56, 0.56, 0.56, 0.56,
                                    0.56, 0.56])

# In mV
chosen_voltage = np.array([500, 500, 500, 500, 500, 500, 200, 200, 200, 200, 200, 200, 200, 100, 100, 100, 100, 100,
                           100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
chosen_voltage_2= 50
print(amplitude_pixel_heights[0] / box_height_in_pixels)

print(len(oscilloscope_frequencies), len(amplitude_pixel_heights), len(voltage_dimensions), len(chosen_voltage))

amplitudes = chosen_voltage * amplitude_pixel_heights / box_height_in_pixels / 1000
conservative_amplitudes = chosen_voltage * amplitude_conservative_pixel_heights / box_height_in_pixels / 1000
amplitudes_2 = (chosen_voltage_2*amplitude_pixel_heights_2 / box_height_in_pixels /1000)
frequencies_2 = oscilloscope_frequencies_2
frequencies = oscilloscope_frequencies

# Definiere die Funktion, die angepasst werden soll
def basic_exponential(x, a, b, c):
    return a * np.exp(-b * x) + c


def basic_reciprocal(x, a, b):
    return a / x + b


# Fitting der Daten mit curve_fit
popt, pcov = curve_fit(basic_exponential, frequencies, amplitudes, p0=[2, 0.00035, 0.1])


# Ausgeben der besten Parameter
print("Best Fit Parameters:")
for i, val in enumerate(popt):
    print(f"{chr(97 + i)} = {val}")

# Berechnen der Standardabweichungen (Fehler der Parameter)
perr = np.sqrt(np.diag(pcov))

print("\nParameter Errors (Standard deviations):")
for i, val in enumerate(perr):
    print(f"{chr(97 + i)} = {val}")


plt.figure(figsize=(12, 5))
plt.title('Chopper frequency against voltage amplitude', fontsize=16)
plt.xlabel('Chopper frequency in [Hz]', fontsize=13)
plt.ylabel('Voltage amplitude in [mV]', fontsize=13)

plt.scatter(frequencies, amplitudes, label='initial')
plt.scatter(frequencies, conservative_amplitudes, label='conservative')
plt.scatter(frequencies_2, amplitudes_2, label='day 2')
# Plot der angepassten Kurve
plt.plot(frequencies, basic_exponential(frequencies, *popt), label="Fitted function", color="red")
# plt.plot(frequencies, basic_exponential(frequencies, 2050, 0.00035, 75), label="Fitted function", color="red")
plt.plot(frequencies, basic_exponential(frequencies, popt[0] + perr[0], popt[1] - perr[1], popt[2] + perr[2]),
         label=r"1-$\sigma$ confidence band", color="k", ls='--', lw=0.75)
plt.plot(frequencies, basic_exponential(frequencies, popt[0] - perr[0], popt[1] + perr[1], popt[2] - perr[2]),
         color="k", ls='--', lw=0.75)

plt.tight_layout()
plt.legend()
plt.savefig('chopper_frequency_against_amplitude.png', dpi=200)
plt.show()
