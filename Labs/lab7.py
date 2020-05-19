# -*- coding: utf-8 -*-

import numpy as np, math as mp
import scipy.integrate as integrate
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# coefficients
k0 = 8.6173303e-5  # Boltzmann constant
k0SI = 1.38064852e-23
m0 = 9.10938356e-31  # electron mass
h = 4.135667662e-15 / (2 * np.pi)  # Plank constant(eV)
hSI = 6.626070040e-34 / (2 * np.pi)  # Plank constant(SI)
ev_joule = 1.60218e-19  # translate eV in 1 Joule
eps_g = 1.21  # ширина забороненої зони AsGa
eps_p = 0.31  # глибина залягання домішки Ti in AsGa
# B
eps_n = 0.00045
a = 1.11e-10

# концентрація домішок
Nd = 2e21  # донорної
Na = 0.1 * Nd  # акцепторної
# ефективні маси в підзонах
mp1 = 0.6 * m0
mn1 = 0.6 * m0
mn2 = 0.6 * m0
mp2 = 0.6 * m0


# zeta - рівень Fermi, T- температура
def DispersionLawNonParabolic(k, n_p, dzeta):
    A = 1.348e-18
    B = 2.697e-35
    if (n_p == True):  # для підзони в зоні провідності
        return - A * k ** 2 + B * k ** 4 - dzeta
    else:  # для рідзони у валентній зоні
        return dzeta + A * k ** 2 - B * k ** 4


# параболічні закони дісперсії
def DispersionLawParabolic(k, n_p, dzeta):
    if (n_p == True):
        A = hSI ** 2 / (2 * mn1 * ev_joule)
        return A * k ** 2 - dzeta
    else:
        A = hSI ** 2 / (2 * mn1 * ev_joule)
        return dzeta - A * k ** 2


def f0(k, dzeta, T, n_p):
    return 1 / (1 + np.exp((DispersionLawParabolic(k, n_p, dzeta)) / (k0 * T)))


def f0_np(k, dzeta, T, n_p):
    return 1 / (1 + np.exp((DispersionLawNonParabolic(k, n_p, dzeta)) / (k0 * T)))


def brillouin_zone_integral(dzeta, T, n_p):
    return 4 * integrate.quad(lambda k: f0(k, dzeta, T, n_p), 0, np.pi / a)[0] / ((2 * np.pi) ** 3)


def brillouin_zone_integral_non_parabolic(dzeta, T, n_p):
    return 4 * integrate.quad(lambda k: f0_np(k, dzeta, T, n_p), 0, np.pi / a)[0] / ((2 * np.pi) ** 3)


# Умова електронейтральності
def ElectroNeutralityCondition(zeta, T):
    ln_na = mp.log(Na) - mp.log((1 + 2 * np.exp(-(zeta - eps_n) / (k0 * T))));
    # print(ln_na)
    na = mp.exp(ln_na)
    nd = mp.log(Nd) - mp.log((1 + 2 * np.exp((zeta - (-eps_g + eps_p)) / (k0 * T))));
    nd = mp.exp(nd)

    # Electroneutralty condition
    NA = brillouin_zone_integral(zeta, T, True) + brillouin_zone_integral_non_parabolic(zeta, T, True);  # electrons
    NH = brillouin_zone_integral(zeta, T, False) + brillouin_zone_integral_non_parabolic(zeta, T, False);  # holes

    A = NA + na - nd - NH

    return A


# Чисельна похідна
def DerivativeElectroNeutralityCondition(zeta, T):
    dx = 1e-5
    return (ElectroNeutralityCondition(zeta + dx, T) - ElectroNeutralityCondition(zeta - dx, T)) / (2 * dx)


# Пошук кореня
def FindRoot(zeta0, T):
    # Точність чисельної похідної
    A = 1e18
    dA = 0
    zeta = zeta0
    i = 0
    while (abs(A) > 10000) & (i < 50):
        A = ElectroNeutralityCondition(zeta, T)
        dA = DerivativeElectroNeutralityCondition(zeta, T)
        if (dA == 0):
            zeta = np.random.rand()
            continue
        zeta = zeta - A / dA
        i = i + 1

    return zeta


N = 50
T = np.zeros([int(N)])
E = np.zeros([int(N)])
# початкове припущення рівня Фермі
zeta = 0

# Залежність рівня фермі від температури
for t in range(N):
    TT = 10 * t + 10
    zeta = FindRoot(zeta, TT)
    # print(TT);
    E[t] = zeta
    T[t] = TT

plt.plot(T, E, lw=2)
plt.xlabel('T, K')
plt.ylabel('Fermi level, eV')
plt.grid(True)
plt.show()

# -*- coding: utf-8 -*-

import numpy as np, math as mp
import scipy.integrate as integrate, matplotlib.pyplot as plt

# coefficients
k0 = 8.6173303e-5  # Boltzmann constant
k0SI = 1.38064852e-23
m0 = 9.10938356e-31  # electron mass
h = 4.135667662e-15 / (2 * np.pi)  # Plank constant(eV)
hSI = 6.626070040e-34 / (2 * np.pi)  # Plank constant(SI)
ev_joule = 1.60218e-19 # translate eV in 1 Joule
eps_g = 1.21  # ширина забороненої зони AsGa
eps_p = 0.31  # глибина залягання домішки Ti in AsGa
# B
eps_n = 0.045
a = 1.11e-10

# концентрація домішок
Nd = 2e22  # донорної
Na = 0.1 * Nd  # акцепторної
# ефективні маси в підзонах
mp1 = 0.6 * m0
mn1 = 0.6 * m0
mn2 = 0.6 * m0
mp2 = 0.6 * m0


# zeta - рівень Fermi, T- температура
def DispersionLawNonParabolic(k, n_p, dzeta):
    A = 1.348e-18
    B = 2.797e-35
    if (n_p == True):  # для підзони в зоні провідності
        return - A * k ** 2 + B * k ** 4 - dzeta
    else:  # для рідзони у валентній зоні
        return dzeta + A * k ** 2 - B * k ** 4


# параболічні закони дісперсії
def DispersionLawParabolic(k, n_p, dzeta):
    if (n_p == True):
        A = hSI ** 2 / (2 * mn1 * ev_joule)
        return A * k ** 2 - dzeta
    else:
        A = hSI ** 2 / (2 * mn1 * ev_joule)
        return dzeta - A * k ** 2


def f0(k, dzeta, T, n_p):
    return 1 / (1 + np.exp((DispersionLawParabolic(k, n_p, dzeta)) / (k0 * T)))


def f0_np(k, dzeta, T, n_p):
    return 1 / (1 + np.exp((DispersionLawNonParabolic(k, n_p, dzeta)) / (k0 * T)))


def brillouin_zone_integral(dzeta, T, n_p):
    return 4 * integrate.quad(lambda k: f0(k, dzeta, T, n_p), 0, np.pi / a)[0] / ((2 * np.pi) ** 3)


def brillouin_zone_integral_non_parabolic(dzeta, T, n_p):
    return 4 * integrate.quad(lambda k: f0_np(k, dzeta, T, n_p), 0, np.pi / a)[0] / ((2 * np.pi) ** 3)


# Умова електронейтральності
def ElectroNeutralityCondition(zeta, T):
    ln_na = mp.log(Na) - mp.log((1 + 2 * np.exp(-(zeta - eps_n) / (k0 * T))))
    # print(ln_na)
    na = mp.exp(ln_na)
    nd = mp.log(Nd) - mp.log((1 + 2 * np.exp((zeta - (-eps_g + eps_p)) / (k0 * T))))
    nd = mp.exp(nd)

    # Electroneutralty condition
    NA = brillouin_zone_integral(zeta, T, True) + brillouin_zone_integral_non_parabolic(zeta, T, True) # electrons
    NH = brillouin_zone_integral(zeta, T, False) + brillouin_zone_integral_non_parabolic(zeta, T, False)  # holes

    A = NA + na - nd - NH

    return A


# Чисельна похідна
def DerivativeElectroNeutralityCondition(zeta, T):
    dx = 1e-5
    return (ElectroNeutralityCondition(zeta + dx, T) - ElectroNeutralityCondition(zeta - dx, T)) / (2 * dx)


# Пошук кореня
def FindRoot(zeta0, T):
    # Точність чисельної похідної
    A = 1e18
    dA = 0
    zeta = zeta0
    i = 0
    while (abs(A) > 10000) & (i < 50):
        A = ElectroNeutralityCondition(zeta, T)
        dA = DerivativeElectroNeutralityCondition(zeta, T)
        if (dA == 0):
            zeta = np.random.rand()
            continue
        zeta = zeta - A / dA
        i = i + 1

    return zeta


N = 50
T = np.zeros([int(N)])
E = np.zeros([int(N)])
# початкове припущення рівня Фермі
zeta = 0

# Залежність рівня фермі від температури
for t in range(N):
    TT = 10 * t + 10
    zeta = FindRoot(zeta, TT)
    # print(TT);
    E[t] = zeta
    T[t] = TT

plt.plot(T, E, lw=2)
plt.xlabel('T, K')
plt.ylabel('Fermi level, eV')
plt.grid(True)
plt.show()