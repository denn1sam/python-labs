import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math

import numpy
import pylab

from mpl_toolkits.mplot3d import Axes3D
V0, Vphi, Vtheta = 200, numpy.pi / 3, numpy.pi / 2
B, Bphi, Btheta = 3, numpy.pi / 3, numpy.pi / 6
E = 100
q = 1.61e-19
m = 1e-24
Bx = B * numpy.cos(Bphi) * numpy.sin(Btheta)
By = B * numpy.sin(Bphi) * numpy.sin(Btheta)
Bz = B * numpy.cos(Btheta)
Vx = V0 * numpy.cos(Vphi) * numpy.sin(Vtheta)
Vy = V0 * numpy.sin(Vphi) * numpy.sin(Vtheta)
Vz = V0 * numpy.cos(Vtheta)
n = 1000
dt = 0.0000001
x, y, z = [0], [0], [0]
while n > 0:
    x.append((Vy * Bz - Vz * By) * q * dt / m + x[len(x) - 1])
    y.append((Vz * Bx - Vx * Bz + E) * q * dt / m + y[len(y) - 1])
    z.append((Vx * By - Vy * Bx) * q * dt / m + z[len(z) - 1])
    Vx += ((Vy * Bz - Vz * By) * q * dt / m)
    Vy += ((Vz * Bx - Vx * Bz + E) * q * dt / m)
    Vz += ((Vx * By - Vy * Bx) * q * dt / m)
    n -= 1
axes = Axes3D(plt.figure())
axes.plot3D(x, y, z)
axes.set_title("Moving of charged body in electric field")
axes.set_xlabel('x', color='blue')
axes.set_ylabel('y', color='red')
axes.set_zlabel('z', color='green')
plt.show()
