'''
The problem in plain words

You have a camera and a 10-unit-long stick placed straight in front of it, facing the camera. You move the stick farther and farther away, from 10 units up to 1000 units. At each distance, work out how long the stick looks in the camera’s image. Then plot “how long it looks” against “how far away it is.”

It’s a 2D world, so the camera’s image is just a line rather than a rectangle, and every point becomes a single number on that line. The focal length f = 1 means the sensor sits 1 unit behind the pinhole.

'''

"""
Perspective projection of a line segment onto a 1-D sensor
==========================================================

Setup (a 2-D world seen from above):
  - A pinhole camera sits at the origin, looking along the +Z axis.
  - A stick 10 units long runs from (-5, Z) to (5, Z), i.e. it faces the camera.
  - The sensor is a 1-D line at distance f = 1 behind the pinhole.

Goal:
  For every distance Z from 10 to 1000, project both ends of the stick
  onto the sensor, measure how long the stick looks there, and plot
  that length against Z.

Key formula (perspective projection, from similar triangles):
      x_image = f * x / Z
"""

import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# 1. Parameters
# ----------------------------------------------------------------------
f = 1.0                 # focal length: distance from pinhole to sensor

x_left = -5.0           # x-coordinate of the stick's left end
x_right = 5.0           # x-coordinate of the stick's right end

# 1000 evenly spaced distances between 10 and 1000.
# More samples just makes the curve smoother.
Z_values = np.linspace(10, 1000, 1000)


# ----------------------------------------------------------------------
# 2. The projection function
# ----------------------------------------------------------------------
def project(x, Z, f):
    """
    Project a 2-D world point (x, Z) onto a 1-D sensor.

    The ray from the point passes through the pinhole. By similar
    triangles, x_image / f = x / Z, so x_image = f * x / Z.

    Works for single numbers or NumPy arrays of Z.
    """
    return f * x / Z


# ----------------------------------------------------------------------
# 3. Simulate: project both endpoints for every Z
# ----------------------------------------------------------------------
# NumPy handles the whole array at once, so no explicit loop is needed.
# Each line below gives one projected position per Z value.
left_on_sensor = project(x_left, Z_values, f)     # equals -5 / Z
right_on_sensor = project(x_right, Z_values, f)   # equals  5 / Z

# Length of the image = distance between the two projected points.
projected_length = right_on_sensor - left_on_sensor   # equals 10 / Z


# ----------------------------------------------------------------------
# 4. Sanity check: compare with the closed-form answer 10 / Z
# ----------------------------------------------------------------------
true_length = x_right - x_left                 # 10 units in the world
expected = f * true_length / Z_values          # 10 / Z
assert np.allclose(projected_length, expected), "Simulation does not match formula!"

# Print a few sample values so the trend is visible in the console.
print(f"{'Z':>8} | {'projected length':>16}")
print("-" * 28)
for Z in [10, 20, 50, 100, 200, 500, 1000]:
    length = project(x_right, Z, f) - project(x_left, Z, f)
    print(f"{Z:>8} | {length:>16.4f}")


# ----------------------------------------------------------------------
# 5. Plot the results
# ----------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

# Left plot: ordinary axes. You should see a hyperbola that falls
# steeply at first and then flattens out.
ax1.plot(Z_values, projected_length, linewidth=2)
ax1.set_xlabel("Distance to camera, Z")
ax1.set_ylabel("Projected length on sensor")
ax1.set_title("Apparent size vs. distance")
ax1.grid(True, alpha=0.3)

# Mark a few points to show "double the distance, half the size".
for Z_mark in [10, 20, 40]:
    L = f * true_length / Z_mark
    ax1.plot(Z_mark, L, "o", color="tab:red")
    ax1.annotate(f"Z={Z_mark}\nL={L:.2f}", (Z_mark, L),
                 textcoords="offset points", xytext=(10, 5), fontsize=9)

# Right plot: log-log axes. Because length = 10 * Z^(-1),
# taking logs gives log(length) = log(10) - log(Z):
# a straight line with slope -1.
ax2.loglog(Z_values, projected_length, linewidth=2)
ax2.set_xlabel("Distance to camera, Z (log scale)")
ax2.set_ylabel("Projected length (log scale)")
ax2.set_title("Same data on log-log axes: straight line, slope = -1")
ax2.grid(True, which="both", alpha=0.3)

plt.tight_layout()
plt.show()