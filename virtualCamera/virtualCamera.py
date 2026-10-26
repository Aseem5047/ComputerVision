'''
The big idea

A screen is flat, but the world is 3D. This experiment shows how to draw a 3D cube on a flat screen so it still looks 3D. The trick is something you already know from real life: things that are farther away look smaller. The whole program is just this rule turned into maths.

Now the 6 faces make sense in the picture:

Front face: the big outer square. It’s closest to you, so it looks biggest. Think of it as the open top of a box, so you can see straight through it.
Back face: the small inner square. Farthest away, so it looks smallest.
Top, bottom, left, right faces: the 4 slanted shapes between the two squares. In real life these are perfect squares too, but because they stretch away from you (from near to far), they get squeezed into those tilted, trapezoid shapes.

And the 12 edges are just all the lines you can see: 4 around the outer square, 4 around the inner square, and the 4 slanted lines joining them.

One thing that might be causing confusion: in real 3D, all 6 faces are identical 2 × 2 squares. None of them is actually bigger or slanted. Every difference you see in the picture comes only from distance, which is exactly what dividing by Z does.

conclusion is the key lesson: the shapes in the picture are not the true shapes. In reality all 6 faces are identical 2 × 2 squares, but the camera shows the near face bigger, the far face smaller, and the side faces squeezed into slanted shapes, purely because of distance. That’s why this matters in computer vision: a computer looking at a photo has to “undo” perspective to figure out the real sizes and shapes of things.

'''

import numpy as np, matplotlib.pyplot as plt

cube = np.array([[x, y, z] for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)], float)
edges = [(i, j) for i in range(8) for j in range(i+1, 8) if np.sum(cube[i] != cube[j]) == 1]

def project(P, f):
    return f * P[:, :2] / P[:, 2:3]          # x = fX/Z, y = fY/Z (all points at once)

p = project(cube + [0, 0, 5], f=1.0)          # cube 5 units in front of the camera
for i, j in edges: plt.plot(*p[[i, j]].T, "k-")
plt.gca().set_aspect("equal"); plt.show()