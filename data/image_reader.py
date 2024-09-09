# Imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
image_index = 1
img = mpimg.imread(f'Oscilloscope data/DS1Z_QuickPrint{image_index}.bmp')

# Display the image
plt.imshow(img)
plt.show()
