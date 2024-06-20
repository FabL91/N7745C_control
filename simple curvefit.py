#provides a small curve fit function, to evaluate T and e when passed luminances
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
import json

c1 = 1.1908E-16#W*m2*str-1
c2 = 1.4388E-2#m*K
calib_temp_a = 0.9884
calib_temp_b = -0.5804

def planck(wv, T, epsilon = 1): #wv must be in micrometers, T in Kelvin
    wv = 1e-6 * wv # convert to metres
    Lech = (epsilon * c1)/(wv**5) * 1/(np.exp(c2/(wv*T)) - 1)
    return Lech * 1E-6 #Unit will be in W.m-2.str-1.um-1

def celsiusToKelvin(tempCelsius):
    return tempCelsius + 273.15

def kelvinToCelsius(tempKelvin):
    return tempKelvin - 273.15

def curveFit(wavelength, luminance, initGuess):#, save_results_to):
    """Fits the sample curve and tries to guess its temperature and emissivity (epsilon)"""
    
    # sigma = [1/luminance[i]**2 for i in range(len(luminance))]
    # print("sigma",sigma)
    fit_results, cov = curve_fit(f=planck, xdata=wavelength, ydata=luminance, p0=initGuess)#, sigma=sigma, absolute_sigma=False) #Fitting the data with the planck function (x->wavelengths, y->luminance)
    #cov is the covariance matrix, fit_results is the temperature and epsilon
    fit_TK, fit_epsilon = fit_results
    x = np.linspace(0.95, 1.65)#Getting a set of data to draw the model curve
    
    plt.plot(x, planck(x, fit_TK, fit_epsilon), color= '#17becf', label=f"model:T={round(fit_TK,2)}K, ε={fit_epsilon:.3e}") #Plotting the fit curve with the estimated parameters (Temperature and epsilon)
    plt.legend()
    plt.ylabel("Luminance [W.m-2.str-1.µm-1]")
    plt.tight_layout()
   # plt.savefig(save_results_to + '/lum_wavelength_sample.png', dpi=300)
    plt.close()
    
    fit_TCel = kelvinToCelsius(fit_TK)#Getting the fitted temperatures (displayed and real)
    fit_Tdisp = (fit_TCel/calib_temp_a)-calib_temp_b
    print("fitT : ",fit_TK,'K <=>', fit_TCel, '°C (real T°), displayed T°=',fit_Tdisp,' \nfit_e:', fit_epsilon)
    
    return fit_Tdisp, fit_epsilon, fit_TK, fit_TCel

lumEdgarcalib010722 = [[9.54E+1,1.84E+2,8.33E+2,1.11E+3],[2.95E+2,5.70E+2,1.99E+3,2.50E+3],[8.03E+2,1.49E+3,4.15E+3,4.96E+3],[1.86E+3,3.23E+3,7.56E+3,8.74E+3],[3.98E+3,6.34E+3,1.28E+4,1.44E+4],[8.20E+3,1.20E+4,2.10E+4,2.29E+4]]
lumEdgarcalib110722 = [[9.07E+1,1.84E+2,8.24E+2,1.10E+3],[2.80E+2,5.56E+2,1.95E+3,2.45E+3],[7.66E+2,1.45E+3,4.07E+3,4.87E+3],[1.79E+3,3.15E+3,7.44E+3,8.59E+3],[3.86E+3,6.22E+3,1.26E+4,1.42E+4],[8.05E+3,1.18E+4,2.08E+4,2.26E+4]]



""" taking the power and ABC coeffcients from the files"""
file="data/Sample19_07_2022_15_31_45continuous_sample_values.json"
dfsample = pd.read_json(file) #Separating json in dataframes
contPower = pd.DataFrame(dfsample['contPower'].tolist()) #getting the power

with open("data/calibration_data.json") as p:
   calibration_data = json.load(p)
   
#Getting the A,B,C values from the files        
Alist = calibration_data["A"]
Blist = calibration_data["B"]
Clist = calibration_data["C"]

measuredLuminanceList = [[0 for j in range(len(Alist))] for i in range(len(contPower))]
for i in range(len(contPower)): #for each power measurement (118)
    for col in range(len(Alist)):#For each photodiode (4)
        print(col)
        #Computing the luminance of the sample from its measured power and stocked A B C values
        measuredLuminanceList[i][col] = pow((contPower[col][i] - float(Blist[col])) / float(Alist[col]), 1/float(Clist[col]))
        if np.imag(measuredLuminanceList[i][col])!=0 :#If the luminance is an imaginary complex, we set it by default at 0
           measuredLuminanceList[i][col] = 0
        print(measuredLuminanceList[i])
        
luminancetofit = measuredLuminanceList #replace the variable here
TCel = []
epsilon = []
for i in luminancetofit:
    fit_Tdisp, fit_epsilon, fit_TK, fit_TCel = curveFit([1.07,1.2,1.55,1.65],i,initGuess = [celsiusToKelvin(400),0.3])
    TCel.append(fit_TCel)
    epsilon.append(fit_epsilon)
    
T=pd.DataFrame(TCel) #convert list to dataframe
E=pd.DataFrame(epsilon)
newdf = pd.concat([T,E],axis=1)
fieldname = ['T','epsilon']
newdf.to_csv("data/Temperature_epsilon_values.csv",index=False,header=fieldname,sep=';') #save to csv
