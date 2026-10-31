import numpy as np, matplotlib.pyplot as plt
f, focus = 50.0, 2000.0                                  # all distances in mm
img_dist = lambda Z: 1 / (1/f - 1/Z)                     # thin lens: z' for object at Z
s, Z = img_dist(focus), np.linspace(500, 10000, 2000)    # sensor position; object range
for N in (1.8, 8):
    A = f / N                                            # aperture diameter from f-number
    plt.plot(Z/1000, A * np.abs(s - img_dist(Z)) / img_dist(Z), label=f"f/{N}")
plt.axhline(0.03, ls="--", c="gray"); plt.ylim(0, 0.3)
plt.xlabel("object distance (m)"); plt.ylabel("blur circle (mm)"); plt.legend(); plt.show()