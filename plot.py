""" plot with a curve_fit function with sigma to add weight"""

#importing libraries
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#importing files
import plck

  
def drawLumPower(wavelength, luminance, power):
    """Draws the power as a function of luminance"""
    p = len(wavelength)
    for j in range(p): #Display the luminance and power for each photodiode
        plt.scatter(luminance[j], power[j])
        print("lumj",luminance[j], "powj",power[j])
    
    plt.title("Power = f(Luminance)")
    plt.legend()
    plt.show()
    print("- - - - - - - - - - - - - - ")


def nonlinearFit(wavelength, luminance, power, save_results_to, name="/power_lum_calib_axcb"):
    """Finds the nonlinear regression of the lines from the drawLumPower function"""
    p = len(wavelength)#Photodiodes
    slopeList = []#Lists of the nonlinear regression coefficients (a*x^c+b)
    interceptList = []
    curveList = []
    for j in range(p):#We take the luminance and power line by line
        # Get slope, intercept, power from curve_fit() to plot y' = intercept + slope*x^curve
        coef_results, cov = curve_fit(f=plck.axcb, xdata=luminance[j], ydata=power[j])
        a, b, c = coef_results
        # Plot nonlinear regression curve.
        print("- - - - - ")
        print("x", luminance[j])
        print("y", power[j])
        print("curve (c)", c)
        print("intercept (b)", b)
        print("slope (a)", a)
        
        y_pred = []#Predicted values of power using the nonlinear model
        i = 0
        while i < len(luminance[j]): #For each column of luminance[j] <=> each temperature
            print("i", i)
            y_pred.append(b + a*luminance[j][i]**c) #y = axc + b 
            i += 1
            print("ypred", y_pred)
            
        print("j", j)
        plt.plot(luminance[j], y_pred, label = f"a{j}={a:.2e};b{j}={b:.2e};c{j}={c:.2e}") #Plotting thee luminance (in X) and the predicted Y (in Y)
        slopeList.append(a)#Adding the slope, intercept and curve to their list
        interceptList.append(b)
        curveList.append(c)
        
    plt.legend(loc='best')    
    plt.xlabel("Luminance [W.m-2.str-1.µm-1]")
    plt.ylabel("Power [W]")
    plt.tight_layout()
    plt.savefig(save_results_to + name + '.png', dpi=300)
    plt.show()
    #plt.clf()
    #plt.cla()
    #plt.close()
    return slopeList, interceptList, curveList


def drawResiduals(wavelength, luminance, fit_T, fit_epsilon, display, save_results_to):
    """Draws residuals vs wavelength"""
    residuals = []
    respercent = []
    lum_fit = []
    print("luminance",luminance)
    print("wv",wavelength)
    for w in range(len(wavelength)):
        lum_fit_temp = plck.planck(wavelength[w], fit_T, fit_epsilon)
        restemp = (luminance[w] - lum_fit_temp)/ lum_fit_temp *100
        res = (luminance[w] - lum_fit_temp)
        residuals.append(float(format(res, '.3e')))
        respercent.append(float(format(restemp,'.3f')))
        lum_fit.append(float(format(lum_fit_temp, '.3e')))
        
    print("residuals",residuals)
    if display:
        plt.scatter(wavelength, residuals, label="Residuals", marker='.')
        plt.title("Residuals")
        plt.xlabel("Wavelength [µm]")
        plt.ylabel("Luminance [W.m-2.str-1.µm-1]")
        plt.tight_layout()
        plt.savefig(save_results_to + '/residuals.png', dpi=300)
        plt.clf()
        plt.cla()
        plt.close()
    return residuals, lum_fit, respercent