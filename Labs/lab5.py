from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math

a = 22*(10**-2)
n = 25 # Point count
q_1 = 5*(10**-9) # First electric current
q_2 = 6*(10**-9) # Second electric current
eps_0 = 8.85e-12 # Electric constant
def phi(x, y):
    r_1  = np.sqrt((a - x) ** 2 + y ** 2)
    r_2  = np.sqrt(x ** 2 + y ** 2)
    k = 1 / (4 * np.pi * eps_0)
    return k * (q_1 / r_2 + q_2 / r_1)/100000
def i_to_x(i):
    return 2 * a * i / n - a / 2.5
def j_to_y(j):
    return a * j / n - a / 2.
u = np.arange(1, n)
X, Y = np.meshgrid(u, u)
V = np.array([phi(x, y) for x, y in zip([i_to_x(i) for i in X],
[j_to_y(j) for j in Y])])
fig = plt.figure()
ax1 = fig.add_subplot(221)
CS=ax1.contour(X, Y, V, levels=7, linewidths=1, colors='k')
plt.clabel(CS,inline=1, fontsize=6)
plt.xlabel('x, mm')
plt.ylabel('y, mm')
ax2 = fig.add_subplot(222, projection="3d")
CS=ax2.plot_surface(X, Y, V, cmap=cm.coolwarm)
plt.xlabel('x, mm')
plt.ylabel('y, mm')
# plt.show()
# fig = plt.figure()
ax = fig.add_subplot(212)
Ex, Ey = np.gradient(V) # Vector field construction
ax.quiver(X, Y, -Ex, -Ey)
plt.show()
