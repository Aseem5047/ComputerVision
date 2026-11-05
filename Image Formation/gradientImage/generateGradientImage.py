
import numpy as np
import matplotlib.pyplot as plt

# Define image dimensions
height = 256
width = 256

# Create an empty RGB image
image = np.zeros((height, width, 3), dtype=float)

# Generate pixel values for each row
for i in range(height):
    # Red channel: i * 0.0039
    image[i, :, 0] = i * 0.0039

    # Green channel: 1 - (i * 0.0039)
    image[i, :, 1] = 1 - i * 0.0039

    # Blue channel: 1
    image[i, :, 2] = 1

# Display the generated image
plt.figure(figsize=(6, 6))
plt.imshow(image)

plt.title("256 x 256 RGB Gradient Image")
plt.axis("off")
plt.show()
