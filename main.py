import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

k1 = 1
k2 = 2
q = 2
H = 40
h = 30
a11 = -q
a13 = -k1/k2 * q
a21 = -q*H
a22 = -(k1/k2)*q*(2*h*H/(h-H))
a33 = (k1/k2)*q*2*h/(h-H)
a12 = -(a11*H**3+a33*h*(h*H-2)+a21*H**2+a22*(h*H-1)+a33*H)/H*(H*h-1)

x = np.linspace(0, H, 100)
y = np.linspace(0, h, 100)
X, Y = np.meshgrid(x, y)
vxy = a11*X**2 + a12*X*Y + a13*Y**2 + a21*X + a22*Y + a33

surface = ax.plot_surface(X, Y, vxy, cmap='viridis')

fig.colorbar(surface, ax=ax, label='vxy')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('vxy')

plt.show()
