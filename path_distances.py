import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

# Given data
kHz_1 = 180 + np.array([-178.5, -179.3, -179.1]) - 0.5
kHz_5 = 180 - np.array([178.2, 178.2, 178.2]) - 0.4
kHz_15 = 180 - np.array([178.9, 178.9, 178.9]) - 0.7

distances = np.array([5*81, 2*81, 81]) * 0.01
delta_t_1 = kHz_1 / 360 / 1000
delta_t_5 = kHz_5 / 360 / 5000
delta_t_15 = kHz_15 / 360 / 15000


slope_1, intercept_1, r_value_1, p_value_1, std_err_1 = stats.linregress(distances, delta_t_1)
slope_5, intercept_5, r_value_5, p_value_5, std_err_5 = stats.linregress(distances, delta_t_5)
slope_15, intercept_15, r_value_15, p_value_15, std_err_15 = stats.linregress(distances, delta_t_15)

line_1 = slope_1 * distances + intercept_1
line_5 = slope_5 * distances + intercept_5
line_15 = slope_15 * distances + intercept_15



plt.plot(delta_t_1, distances, 'o', label='1kHz')
plt.plot(line_1, distances, label=f'1kHz Fit (slope={1/slope_1:.2e})')

plt.plot(delta_t_5, distances, 'o', label='5kHz')
plt.plot(line_5, distances, label=f'5kHz Fit (slope={1/slope_5 if slope_5 != 0 else np.inf:.2e})')

plt.plot(delta_t_15, distances, 'o', label='15kHz')
plt.plot(line_15, distances, label=f'15kHz Fit (slope={1/slope_15 if slope_15 != 0 else np.inf:.2e})')

# Add labels and legends
plt.ylabel('Distances (m)')
plt.xlabel('Delta t (s)')
plt.legend()
plt.title('Distances vs Delta t with Linear Regression (Axes Swapped)')
plt.grid(True)

# Show plot
plt.show()



(slope_1, intercept_1), (slope_5, intercept_5), (slope_15, intercept_15)


