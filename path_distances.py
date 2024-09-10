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

# Calculate the linear regressions
slope_1, intercept_1, r_value_1, p_value_1, std_err_1 = stats.linregress(distances, delta_t_1)
slope_5, intercept_5, r_value_5, p_value_5, std_err_5 = stats.linregress(distances, delta_t_5)
slope_15, intercept_15, r_value_15, p_value_15, std_err_15 = stats.linregress(distances, delta_t_15)

# Generate linear regression lines
line_1 = slope_1 * distances + intercept_1
line_5 = slope_5 * distances + intercept_5
line_15 = slope_15 * distances + intercept_15

# Plot with linear regressions
#plt.plot(distances, delta_t_1, 'o', label='1kHz')
#plt.plot(distances, line_1, label=f'1kHz Fit (slope={slope_1:.2e})')

plt.plot(distances, delta_t_5, 'o', label='5kHz')
plt.plot(distances, line_5, label=f'5kHz Fit (slope={slope_5:.2e})')

plt.plot(distances, delta_t_15, 'o', label='15kHz')
plt.plot(distances, line_15, label=f'15kHz Fit (slope={slope_15:.2e})')


plt.xlabel('Distances (m)')
plt.ylabel('Delta t (s)')
plt.legend()
plt.title('Delta t vs Distance with Linear Regression')
plt.grid(True)


plt.show()


(slope_1, intercept_1), (slope_5, intercept_5), (slope_15, intercept_15)


