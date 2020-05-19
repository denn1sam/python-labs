import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math

T = {}  # euler
Trk = {}  # runge-kutta
tm = []  # timer
accuracy = math.exp(1e-5)
t_environment = 30
t_begin = 100
T[0] = Trk[0] = t_begin
tm.append(0)
r = 0.12
dt = 5
i = 0

while T[i] >= t_environment:
    # Runge kutta
    k1 = r * (Trk[i] - t_environment)
    k2 = r * ((Trk[i] - t_environment) + k1 * dt / 2)
    k3 = r * ((Trk[i] - t_environment) + k2 * dt / 2)
    k4 = r * ((Trk[i] - t_environment) + k3 * dt)
    Trk[i + 1] = Trk[i] - (k1 + 2 * k2 + 2 * k3 + k4) * dt /6
    # Euler
    T[i + 1] = T[i] - r * dt * (T[i] - t_environment)
    tm.append(tm[i] + dt)
    if math.fabs(T[i + 1] - T[i]) <= 1e-5:
        break
    print(T[i])
    i += 1

print('Points: ', i)
plt.subplot()
plt.plot(tm, list(Trk.values()), 'g-.', tm, list(T.values()), 'r--')
plt.xlabel('time, min')
plt.ylabel('T,K')
plt.title('Cup cooling(Euler&Runge-kutta methods)')
plt.grid(True)
plt.legend(['Runge-Kutta', 'Euler'])
plt.show()
