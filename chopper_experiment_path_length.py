# Imports
import numpy as np
from typing import List

# Errors are in [mm]
parallax_error = 1 / np.sqrt(6)
chopper_position_error = 1 / np.sqrt(3)
position_error = 2 / np.sqrt(3)
angular_position_error = 3 / np.sqrt(3)


def get_combined_reading_error(positional_error: float) -> float:
    return np.sqrt(parallax_error ** 2 + positional_error ** 2)


def get_combined_error(errors: List[float]) -> float:
    return np.sqrt(np.sum([error ** 2 for error in errors]))


# Combined errors for different paths
chopper_to_mirror_error = get_combined_error([get_combined_reading_error(chopper_position_error),
                                              get_combined_reading_error(position_error)])

mirror_to_mirror_error = np.sqrt(2) * get_combined_reading_error(position_error)

tilted_mirror_to_mirror_error = np.sqrt(2) * get_combined_reading_error(angular_position_error)

# Path lengths in [mm]
chopper_to_m1 = 437
m1_to_m2 = 812
m2_to_m3 = 811
m3_to_m4 = 810

# Path length and corresponding error
path_length = 2 * (chopper_to_m1 + m1_to_m2 + m2_to_m3 + m3_to_m4)

path_length_error = 2 * get_combined_error([chopper_to_mirror_error, tilted_mirror_to_mirror_error,
                                            tilted_mirror_to_mirror_error, mirror_to_mirror_error])

# Printing out the results
print(f'Parallax error: {round(parallax_error, 2)} mm')
print(f'Chopper to mirror error: {round(chopper_to_mirror_error, 2)} mm')
print(f'Tilted mirror error: {round(tilted_mirror_to_mirror_error, 2)} mm')
print(f'Mirror to mirror error: {round(mirror_to_mirror_error, 2)} mm')
print(f'Path length = ({round(path_length, 2)} ± {round(path_length_error, 2)}) mm')
