import matplotlib.pyplot as plt
from scipy.stats import linregress

#For the blackbody : these are the calibration temperatures 
real_temperature = [691.2, 839.7, 988.0, 1185.3]
displayed_temperature = [700.00, 850.01, 999.99, 1199.87]
save_results_to = 'C:/Users/flepetit/Desktop/Keysight N7745C/N7745C_control/data/calib Test/' #The folder where data will be saved


def fitTemperature(real_temperature = [691.2, 839.7, 988.0, 1185.3], displayed_temperature = [700.00, 850.01, 999.99, 1199.87]):
    displayed = displayed_temperature
    real = real_temperature
    # Get slope, intercept from linregress() to plot y' = intercept + slope*x
    (slope, intercept, rvalue, pvalue, stderr) = linregress(displayed, real)
    
    # Plot linear regression line.
    print("- - - - - ")
    print("x", displayed)
    print("y", real)
    print("b", intercept)
    print("a", slope)

    y_pred = []
    i = 0
    while i < len(displayed): #For each temperature
        y_pred.append(intercept + slope*displayed[i]) #y = ax + b 
        i += 1
        
    print("ypred", y_pred)    
    plt.plot(displayed, real, 'o', label='original data')
    plt.plot(displayed, y_pred, label = f"y=a*x+b\na={slope:.4f}+/-{stderr:.4f};b={intercept:.4f}")
    plt.title("Calibration of the BlackBody source")    
    plt.xlabel("Displayed Temperature [°C]")
    plt.ylabel('Real Temperature [°C]')
    plt.legend()
    # Set labels
    plt.legend(loc='best')
    plt.savefig(save_results_to + 'temperature_calib.png', dpi=300)
    plt.show
    return slope, intercept

fitTemperature()