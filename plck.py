#importing libraries
import numpy as np


c1 = 1.1908E-16#W*m2*str-1
c2 = 1.4388E-2#m*K

calib_temp_a = 0.9884
calib_temp_b = -0.5804

def celsiusToKelvin(tempCelsius):
    return tempCelsius + 273.15


def kelvinToCelsius(tempKelvin):
    return tempKelvin - 273.15


def planck(wv, T, epsilon = 1): #wv must be in micrometers, T in Kelvin
    wv = 1e-6 * wv # convert to metres
    Lech = (epsilon * c1)/(wv**5) * 1/(np.exp(c2/(wv*T)) - 1)
    return Lech * 1E-6 #Unit will be in W.m-2.str-1.um-1


def reversePlanck(wv, Lum, epsilon=1): #wv must be in micrometers, T in Kelvin
    constantA = (c1 * epsilon)
    wv = 1e-6 * wv # convert to metres
    T = c2/wv *(1/(np.log(constantA / (Lum*(wv**5)) + 1)))
    return T

def calculTK(t):
    return celsiusToKelvin((t - calib_temp_b) / calib_temp_a )

def axcb(x, a, b, c):
    return b+a*x**c