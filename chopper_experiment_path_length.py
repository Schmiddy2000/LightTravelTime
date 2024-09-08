# Imports
import numpy as np

# Errors are in [mm]
parallax_error = 1 / np.sqrt(6)
position_error = 2 / np.sqrt(3)
combined_position_error = np.sqrt(parallax_error ** 2 + position_error ** 2)

# What is the chopper to mirror error? And should we treat the m3 to m4 error also differently (angle = 0)?
chopper_to_mirror_error = np.sqrt(2) * parallax_error
mirror_to_mirror_error = np.sqrt(2) * combined_position_error

# Path lengths in [mm]
chopper_to_m1 = 437
m1_to_m2 = 812
m2_to_m3 = 811
m3_to_m4 = 810

path_length = 2 * (chopper_to_m1 + m1_to_m2 + m2_to_m3 + m3_to_m4)

# This might need to be modified in case that we assume different errors (as mentioned above). Or do we have to
# proceed differently anyway, since the error for a given path segment is the same for both directions?
path_length_error = np.sqrt(8 * mirror_to_mirror_error)

print(f'Parallax error: {round(parallax_error, 2)} mm')
print(f'Position error: {round(position_error, 2)} mm')
print(f'Combined position error: {round(combined_position_error, 2)} mm')
print(f'Mirror to mirror error: {round(mirror_to_mirror_error, 2)} mm')
print(f'Path length = ({round(path_length, 2)} ± {round(path_length_error, 2)}) mm')
