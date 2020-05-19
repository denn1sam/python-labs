import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math

start_pos_x = {}
start_pos_y = {}
v = {}
speed_vx = {}
speed_vy = {}
start_time = {}
c = {}
s = {}

alfa = 30
alfa_gr = alfa*math.pi/180     #Start angle
v0 = 40                     #Start speed of body
delta_t = .10  # Time step
speed_vx[0] = v0 * math.cos(alfa_gr)  # Start speed of X
speed_vy[0] = v0 * math.sin(alfa_gr)  # Start speed of Y
start_time[0] = 0  # Start time
start_pos_y[0] = 50  # Start position by Y
start_pos_x[0] = 0  # Start position by X
g = 9.8  # Free fall acceleration speed
mass = 7  # kg
k2 = 10**(-2)  # kg/m

i = 0
A = k2 / mass


while 1:
    v[i] = math.sqrt(speed_vx[i] ** 2 + speed_vy[i] ** 2)
    c[i] = speed_vx[i] / v[i]
    s[i] = speed_vy[i] / v[i]
    #vx[i + 1] = vx[i]
    speed_vx[i + 1] = speed_vx[i] - A * v[i] ** 2 * c[i] * delta_t
    speed_vy[i + 1] = speed_vy[i] - (g + (k2 / mass) * v[i] ** 2 * (speed_vy[i] / v[i])) * delta_t
    start_pos_x[i + 1] = start_pos_x[i] + speed_vx[i + 1] * delta_t
    start_pos_y[i + 1] = start_pos_y[i] + speed_vy[i + 1] * delta_t
    start_time[i + 1] = start_time[i] + delta_t

    #print(vx[i], vy[i])

    if start_pos_y[i + 1] <= 0: break

    i += 1

class Reverse:
    def __init__(self, x,v,t,y):
        self.x = x
        self.v = v
        self.t = t
        self.y = y
        self.j = len(x)
        self.j = len(y)
        self.j = len(v)
        self.j = len(t)
def reverse(x):
    for j in range(len(x)-1):
        yield x[j]
x1 = [0 for j in range(len(start_pos_x) - 1)]
v1 = [0 for j in range(len(v)-1)]
t1 = [0 for j in range(len(start_time) - 1)]
y1 = [0 for j in range(len(start_pos_y) - 1)]

for j in range(0, len(v)-1):
    v1[j] = v[j]
for j in range(0, len(start_time) - 1):
    t1[j] = start_time[j]
for i in range(0, len(start_pos_y) - 1):
    y1[i] = start_pos_y[i]
for i in range(0, len(start_pos_x) - 1):
    x1[i] = start_pos_x[i]

import matplotlib.pylab as pp

pp.figure(1)
pp.subplot(221)
pp.plot(t1, y1,'r-' )
pp.xlabel('t, c')
pp.ylabel('h, m')
pp.title('h(t)')
pp.grid(True)

pp.subplot(222)
pp.plot(x1, y1,'g-')
pp.xlabel('x, m')
pp.ylabel('y, m')
pp.title('XY')
pp.grid(True)


pp.subplot(223)
pp.plot(t1, x1,'b-')
pp.xlabel('t, m')
pp.ylabel('x, m')
pp.title('x')
pp.legend(["x(t)"])
pp.text(7,75,r'$v_0t$+$at^2/2$')
pp.grid(True)

pp.show()
