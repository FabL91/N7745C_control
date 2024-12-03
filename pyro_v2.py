"""ajout d'un delai en mode continu
"""

#A ajouter  : 
#         - indicateur (lumiere) sur la qualite du fit
#         - fichier .exe

#importing libraries
import ast
from datetime import datetime
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyvisa as visa
from scipy.optimize import curve_fit
import sys
import time
import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer, QSize #,QObject
from PyQt5.QtWidgets import QFileDialog, QToolBar, QAction
from PyQt5.QtGui import QIcon, QPixmap

from matplotlib import use
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import logging

#importing files
import application as app #this is where we send commands to measure the power
import plck #planck's equations and a few conversions
import plot #functions that plots or fits
from newpyro_v2 import Ui_Pyro #Interface file
#from mplwidget import MplWidget #Using this to display matplotlib graphs inside QWidgets

#Planck's constants
c1 = 1.1908E-16#W*m2*str-1
c2 = 1.4388E-2#m*K

#Parameters of the linear fit of the blackbody calibration (see blackbody_calibration.py)
calib_temp_a = 0.9884
calib_temp_b = -0.5804

color_list = ['#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b','#bcbd22']

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s', filename='Logging_Pyro.log', level=logging.INFO)

class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure(figsize=(6,4))
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas()# Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)     
    
class Pyro(QtWidgets.QMainWindow):
    def __init__(self):
        super(Pyro, self).__init__() # Call the inherited classes __init__ method
        #Interface setup
        self.ui = Ui_Pyro()
        self.ui.setupUi(self)
        self.setWindowTitle("Pyro")        
        #power meter adress
        self.ui.id_powermeter.addItem('TCPIP0::169.254.241.203::inst0::INSTR')
        self.ui.id_powermeterS.addItem('TCPIP0::169.254.241.203::inst0::INSTR')
        
        #Preparing sample graphs
        self.plotWidgetUp = MplWidget(self.ui.widgetUp)
        self.plotWidgetDown = MplWidget(self.ui.widgetDown)
        self.plotWidgetDown.canvas.ax.set_visible(False)
        self.gs = self.plotWidgetDown.canvas.fig.add_gridspec(2, hspace=0) #For continuous measures, emissivity and temp vs time
        self.plotWidgetDown.canvas.axs = self.gs.subplots(sharex=True)  
        self.plotWidgetDown.canvas.axs[0].set_xlabel("Time (s)")
        self.plotWidgetDown.canvas.axs[0].set_ylabel("Temperature (°C)")
        self.plotWidgetDown.canvas.axs[1].set_ylabel("Emissivity")
        self.plotWidgetDown.canvas.fig.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for any title
        
        #Connection des bouttons pour l'acquisition rapide
        self.ui.nbre_pts.textEdited.connect(self.NbrePts_changed)
        self.ui.Ar_Time.textEdited.connect(self.AverageTime_changed)
        self.ui.List_Unit.addItems(["S", "MS", "US"])
        self.ui.List_Unit.currentTextChanged.connect(self.Unit_changed)
        self.ui.Delay_Read_Buf.textEdited.connect(self.Delay_Read_Buffer_changed)
        
        
        #Connecting buttons to their functions and hidding some that are not useful yet
        self.ui.startButton.clicked.connect(self.startCalib)
        self.ui.startButtonS.clicked.connect(self.startSample)
        self.ui.startContButtonS.clicked.connect(self.startContMode)
        self.ui.okButton.setHidden(True)
        self.ui.labelNbMeasure.setHidden(True)
        self.ui.valNbMeasure.setHidden(True)
        self.ui.labelTempLim.setHidden(True)
        self.ui.temp_limit.setHidden(True)
        self.ui.labelEmlim.setHidden(True)
        self.ui.em_limit.setHidden(True)
        self.ui.stopButton.setHidden(True)
        self.ui.stopButton.clicked.connect(self.stopContMode)
        self.ui.chooseFolder.clicked.connect(self.folder)
        self.ui.chooseFolderS.clicked.connect(self.folder)
        #adding a toolbar to the top left of the GUI, with 4 buttons : open folder, one time measure, continuous measure and quit
        self.toolbar = QToolBar("Toolbar")
        self.toolbar.setIconSize(QSize(32,32))
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolbar)
        
        self.button_folder = QAction(QIcon("images/folder.png"),"Folder",self)
        self.button_folder.triggered.connect(self.folder)
        self.toolbar.addAction(self.button_folder)
        self.button_folder.setShortcut(Qt.CTRL + Qt.Key_O) #CTRL + O to Open folder
    
        self.toolstartButtonS = QAction(QIcon("images/arrow.png"),"One Measure",self)
        self.toolstartButtonS.triggered.connect(self.startSample)
        self.toolbar.addAction(self.toolstartButtonS)
        self.toolstartButtonS.setShortcut(Qt.CTRL + Qt.Key_M) #CTRL + M to Measure once
    
        self.toolstartContButtonS = QAction(QIcon("images/arrow-retweet.png"),"Continuous Measure",self)
        self.toolstartContButtonS.triggered.connect(self.startContMode)
        self.toolbar.addAction(self.toolstartContButtonS)
        self.toolstartContButtonS.setShortcut(Qt.CTRL + Qt.Key_L) #CTRL + L to measure (Loop)
        
        self.stopMode = QAction(QIcon("images/stop.png"),"Stop",self)
        self.stopMode.triggered.connect(self.stopContMode)
        self.toolbar.addAction(self.stopMode)
        self.stopMode.setShortcut(Qt.CTRL + Qt.Key_S) #CTRL + S to Stop the loop
        
        self.toolstartQuit = QAction(QIcon("images/cactus.png"),"Quit",self)
        self.toolstartQuit.triggered.connect(self.fileQuit)
        self.toolbar.addAction(self.toolstartQuit)
        self.toolstartQuit.setShortcut(Qt.CTRL + Qt.Key_Q) #CTRL + Q to Quit
        
        self.ui.checkBoxBounds.stateChanged.connect(self.boolBounds)#When we check / uncheck the box
        self.ui.checkBoxSigma.stateChanged.connect(self.boolSigma) #it connects to the functions below
        self.bounds = False
        self.sigma = False
        
    def boolBounds(self):
        self.bounds = self.ui.checkBoxBounds.isChecked()
        print("bounds?",self.bounds)
        
    def boolSigma(self):
        self.sigma = self.ui.checkBoxSigma.isChecked()
        print("sigma?",self.sigma)
        
        
    def setValPowS(self, val): #functions to set values in the GUI
        self.ui.valPowS.setText(val)    #power sample
        
    def setValLum(self, val):
        self.ui.valLuminance.setText(val) #luminance sample
        
    def setValFitLum(self, val): #Fit luminance values
        self.ui.valFitLum.setText(val)
        
    def setValRes(self, val):
        self.ui.valResiduals.setText(val) #fitted luminance
    
    def setValResPercent(self, val): #residuals in %
        self.ui.valResidualsP.setText(val)
        
    def setValEps(self, val): #eps = epsilon = emissivity
        self.ui.valEps.setText(val)
    
    def setValTemp(self, val):
        self.ui.valTemp.setText(val) #temperature
        
    def setValNbMeas(self, val):
        self.ui.valNbMeasure.setText(val) #number of measures
    
    
    def fileQuit(self):
        self.close() 
        
        
    def saveJson(self,variable_name,file_name, write='w'):
        """Two functions to open and save Json files"""
        with open(self.cdir + f"{file_name}.json", write, encoding='utf-8') as var:
            json.dump(variable_name, var, ensure_ascii=False, indent=2)#Writing the values from the files  


    def openJson(self,file):
        try :
             with open(self.cdir + f"{file}.json") as p:
                return json.load(p)
        except AttributeError:
            print("The save file has not been found in the current folder")
        else :
            with open(f"{file}.json") as p:
               return json.load(p)
     
    def folder(self):
        """chooses the folder where the files will be saved """
        #current directory
        self.cdir = QFileDialog.getExistingDirectory(self) +'/' #Current directory
        self.ui.labelDir.setText(self.cdir)
        self.ui.labelDirS.setText(self.cdir)
        self.default()
    
    
    def default(self):
        """fills in the labels with the values from the parameters file (parameters.json)"""
        self.par = self.openJson("parameters")
        print(self.cdir + "parameters")        
        self.temperature = self.par["temperature_ListCel"]
        self.wavelengths = self.par["wavelengths"]
        self.avgTime = self.par["average_time"]

        #intialise les controls de l'acquisition rapide
        self.nbre_pts = self.par["nbre_pts"]
        self.Aver_Time = self.par["Ar_Time"]
        self.unit = self.par["List_Unit"]
        
        #calibration tab        
        self.ui.temperature.setText(str(self.par["temperature_ListCel"]))
        self.ui.wavelength.setText(str(self.par["wavelengths"]))    
        self.ui.avg_time.setText(str(self.par["average_time"]))
        self.ui.nbre_pts.setText(self.par["nbre_pts"])
        self.ui.Ar_Time.setText(self.par["Ar_Time"])
        self.ui.List_Unit.setCurrentText(self.par["List_Unit"])
        self.Delay_R_Buf = self.par["Delay_Read_Buf"]
        self.ui.Delay_Read_Buf.setText(self.par["Delay_Read_Buf"])

        
        
        #sample tab
        self.ui.avg_timeS.setText(str(self.par["average_time"]))
        self.ui.em_limit.setText(str(self.par["epsilonLimits"]))
        self.ui.temp_limit.setText(str(self.par["temperatureLimits"]))
        self.ui.init_guess.setText(str(self.par["init_guess"]))
        self.ui.delay.setText(str(self.par["delay"]))
        
    """End of interface control functions"""
    
    """Start of Instrument control functions"""
    
    
    def Errorcheck(self, N7745C):
        """Checking for error messages coming from the instrument"""
        self.myError = []
        self.ErrorList = N7745C.query("SYST:ERR?").split(',')
        self.error = self.ErrorList[0]
        
        if int(self.error) == 0:
            print ("+0, No Error!")
            
        else:
            while int(self.error)!=0:
                print ("Error #: " + self.ErrorList[0])
                print ("Error Description: " + self.ErrorList[1])
                
                self.myError.append(self.ErrorList[0])
                self.myError.append(self.ErrorList[1])
        
                self.ErrorList = N7745C.query("SYST:ERR?").split(',')
                self.error = self.ErrorList[0]
                self.myError = list(self.myError)
                
        return self.myError
    
    
    def connection(self):
        """Connects to the instrument"""
        self.rm = visa.ResourceManager() #visa connection
        #self.N7745C = self.rm.open_resource('TCPIP0::100.65.4.185::inst0::INSTR')
        self.N7745C = self.rm.open_resource('TCPIP0::169.254.241.203::inst0::INSTR')
        self.N7745C.timeout = 10000
        self.N7745C.write("*CLS")#Clear the event status registers and empty the error queue
        self.N7745C.write("*IDN?")#Query identification string *IDN?
        print(self.N7745C.read())
        if self.Errorcheck(self.N7745C) == []: #8 channels on the N7745C
            self.val_run = True
        
            #Presets the N7745C and wait for operation complete via the *OPC?, i.e.
            #the operation complete query.
            self.N7745C.write("SYST:PRES;*OPC?")
            print("Preset complete, *OPC? returned : " + self.N7745C.read())
                
            self.N7745C.write(':configure:measurement:setting:preset')#Resets the settings            
            #self.N7745C.write(':sense:power:unit:all Watt')#Sets the sensor power unit of all channels to Watt
            #self.N7745C.write(':sense1:power:gain:auto 1')#auto gain
            print('\n------------------------\n')
            
            
    def initiate(self):
        """Sets the wavelength for every photodiode"""
        wvUnit = 'um'            
        for w in self.wavelengths:
            i = self.wavelengths.index(w)#Index of the loop (starting from 0)
            #I think there was a reason I did a loop using .index(w) instead of changing to wavelengths[i]
            #If the wavelength is twice the same, it could be a problem here
            if w <= 1.250:#N7745C only accept as a parameter wavelengths between 1250 and 1650nm
                #Sets the sensor wavelength and its unit.
                self.N7745C.write(f'sense{i+1}:power:wavelength {1.250}{wvUnit}')
                print(f"set wavelength n°{i} to {w}{wvUnit}")
                
            elif w >= 1.650:
                #Sets the sensor wavelength and its unit.
                self.N7745C.write(f'sense{i+1}:power:wavelength {1.650}{wvUnit}')
                print(f"set wavelength n°{i} to {w}{wvUnit}")
                
            else:       
                #Sets the sensor wavelength and its unit.
                self.N7745C.write(f'sense{i+1}:power:wavelength {w}{wvUnit}')
                print(f"set wavelength n°{i} to {w}{wvUnit}")
                
                
    def setAveragingTime(self,avg):
        for i in range(len(avg)):#for each averaging time in the list
            a = avg[i]
            self.N7745C.write(f"sense{i+1}:power:atime {a}ms") #in milliseconds

    """ End of instrument control functions"""  
         
    """ Start of Calibration functions"""
    
    
    def getParametersCalib(self):
        """gets the values from the labels of calibration tab and places them in the parameters file"""
        par = self.openJson("parameters")
        #calibration tab
        try :
            par["temperature_ListCel"] = ast.literal_eval(self.ui.temperature.text())
            par["wavelengths"] = ast.literal_eval(self.ui.wavelength.text())
            par["average_time"] = ast.literal_eval(self.ui.avg_time.text())
            par["id_powermeter"] = self.ui.id_powermeter.currentText()
        except TypeError:
            print("Wrong parameters format")
            
        self.saveJson(par,"parameters")    
        self.temperature = par["temperature_ListCel"]
        self.wavelengths = par["wavelengths"]
        self.avgTime = par["average_time"]
        
        self.temperatureListK = []
        print(self.temperature)
        #Calibrating the temperature using the data from the blackbody calibration
        #taking into account the difference between measured and displayed blackbody temperatures
        for t in self.temperature: 
            #y=ax+b where x is the displayed temperature on the black body interface, y is the real temperature
            self.temperatureListK.append(plck.celsiusToKelvin(calib_temp_a*t+calib_temp_b))
        par["temperatureListK"] = self.temperatureListK
        
        self.saveJson(par,"parameters")
    
    
    def calibVariables(self):        
        """"Defining the variables for calibration"""
        self.p = len(self.wavelengths) #Number of photodiodes
        self.n = len(self.temperatureListK) #Number of temperatures
        self.returnedpower = [[0 for i in range(self.n)] for j in range(self.p)]#Final matrices of power and luminance values 
        self.returnedlum = [[0 for i in range(self.n)] for j in range(self.p)]
        self.Alist = [0 for j in range (self.p)]
        self.Blist = [0 for j in range(self.p)]  
        self.Clist = [0 for j in range(self.p)]
        self.index = 0 #index of the current temperature
        
        
    def startCalib(self):
        """Starts the calibration by getting variables"""
        self.getParametersCalib()
        self.calibVariables() #Initializing variables
        self.connection() #connecting to the instrument
        self.initiate() #initiating the instrument
        #self.setAveragingTime(self.avgTime)
        app.Init_Mesure(window.N7745C, self.nbre_pts, self.Aver_Time, self.unit)
        self.power_calib_reduced = []
        self.luminance_calib_reduced = []
    
        if self.val_run:
            print("start")
            #Changing Start and Ok Buttons
            self.ui.okButton.setHidden(False)
            self.ui.okButton.setEnabled(True)
            self.ui.startButton.setEnabled(False)
            self.ui.startButton.setHidden(True)
            self.ui.textTemperature.setText(f"Press OK when the measurement is ready to be made at {self.temperature[0]}[@°C]")
            #self.ui.textTemperature.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.textTemperature.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignJustify)
            self.ui.okButton.clicked.connect(self.calibMain)
        else:
            print("ErrorCheck : X")


    def calibMain(self):
        print("calibMain")
        
        self.returnedpower, self.returnedlum = app.calibration(
            self.N7745C, self.temperatureListK, self.temperatureListK[self.index], 
            self.returnedpower, self.returnedlum, self.wavelengths)
       
        self.calibration_data = self.openJson("calibration_data")
        
        self.calibration_data["power_calib"] = self.returnedpower#Writing the power and luminance values in their files
        self.calibration_data["lum_calib"] = self.returnedlum
        self.saveJson(self.calibration_data, "calibration_data")
        self.ui.valPow.setText(str(self.returnedpower))
        self.ui.valLum.setText(str(self.returnedlum))
        
        self.index += 1
        
        if self.index < self.n:
            #Changing the label with the next temperature
            self.ui.textTemperature.setText(f"Press OK when the measurement is ready to be made at {self.temperature[self.index]}[@°C]")
            self.ui.textTemperature.setAlignment(Qt.AlignmentFlag.AlignCenter)
        elif self.index == self.n: #When we measured all temperatures
        
            #Plotting and fitting the data
            plot.drawLumPower(self.wavelengths, self.returnedlum, self.returnedpower)
            try : 
                self.Alist, self.Blist, self.Clist = plot.nonlinearFit(self.wavelengths, self.returnedlum, self.returnedpower, self.cdir)#Applying a nonlinear regression model
            except RuntimeError:
                print("Not able to fit the curve")
                
            #Modifying buttons and labels to be able to reset
            self.ui.textTemperature.setText("")
            self.ui.startButton.setText("Reset")
            self.ui.startButton.setEnabled(True)
            self.ui.startButton.clicked.connect(self.resetCalib)
            self.ui.startButton.setHidden(False)
            self.ui.okButton.setHidden(True)
                    
            #Writing the power and luminance values in their files
            self.calibration_data["A"] = self.Alist
            self.calibration_data["B"] = self.Blist
            self.calibration_data["C"] = self.Clist
            print("\nAlist",self.Alist)  
            print("\nBlist",self.Blist)
            print("\nClist",self.Clist)
            self.saveJson(self.calibration_data, "calibration_data")
            
            self.N7745C.close() #Closing the link with the instrument
            self.rm.close()
            
            #Plotting the graph
            self.ui.labelgraphUp.setPixmap(QPixmap(self.cdir + "/power_lum_calib_axcb.json"))
            self.ui.labelgraphUp.setScaledContents(True)
            
    
    def resetCalib(self):        
        self.ui.startButton.clicked.connect(self.startCalib)
        self.ui.startButton.setText("Start")
        self.ui.startButton.setEnabled(True)
        self.ui.textTemperature.setText("Press Start when ready to measure")
        

    """end of calibration functions"""
    
    """start of sample functions"""
    
    def getParametersSample(self):
        """gets the values from the labels of sample tab and places them in the parameters file"""
        par = self.openJson("parameters")
        #sample tab
        try:#ast allows to get the list in the right format
            par["avg_timeS"] = ast.literal_eval(self.ui.avg_timeS.text()) 
            par["epsilonLimits"]= ast.literal_eval(self.ui.em_limit.text())
            par["temperatureLimits"] = ast.literal_eval(self.ui.temp_limit.text())
            par["init_guess"] = ast.literal_eval(self.ui.init_guess.text())
            par["delay"] = ast.literal_eval(self.ui.delay.text())
        except:
            print("Wrong parameters format")
            
        self.avgTimeS=par["avg_timeS"] #avgTimeS --> S=sample
        self.saveJson(par,"parameters")
        
        self.t0 = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
        self.tinit = time.time() #almost the same time as t0, but in a different format, to be able to use it for a time scale
        #Creating a folder for the measurement
        self.sampleFolder = "Sample" + self.t0
        print("sample folder :", self.sampleFolder)

            
    def startSample(self):
        """Starts measuring sample (just once)"""
        print("start sample")
        self.worker = ThreadMeasure()
        self.worker.running=False #Not a continuous measurement
        
        self.getParametersSample()
        self.connection() #connecting to the instrument
        self.initiate() #initiating
        #self.setAveragingTime(self.avgTimeS)
        app.Init_Mesure(window.N7745C, self.nbre_pts, self.Aver_Time, self.unit)
        self.worker.start() #starting the measurement thread
        self.connectSignals()
        
    
    def startContMode(self):
        """Starts the continuous measurement"""
        print("start continuous sample")
        #Changing Start and Stop Buttons
        self.ui.stopButton.setHidden(False)
        self.ui.stopButton.setEnabled(True)           
        self.ui.startButtonS.setHidden(True)
        self.ui.startContButtonS.setHidden(True)
        self.ui.labelNbMeasure.setHidden(False)
        self.ui.valNbMeasure.setHidden(False)
        
        #For the sample measurement
        self.worker = ThreadMeasure()
        self.worker.running = True #Indicates whether the measure should keep going or not after the 1st iteration
        
        self.getParametersSample()
        self.connection() #connecting to the instrument
        self.initiate() #initiating
        self.sample_values = {}
        self.saveJson(self.sample_values, window.sampleFolder + "continuous_sample_values", 'w+')
   
        #self.setAveragingTime(self.avgTimeS)
        app.Init_Mesure(window.N7745C, self.nbre_pts, self.Aver_Time, self.unit)
        self.worker.start() #starting the measurement thread
        self.connectSignals()
        
        
    def connectSignals(self):
        self.worker.resultPow.connect(self.setValPowS)
        self.worker.resultLum.connect(self.setValLum)
        self.worker.resultFitLum.connect(self.setValFitLum)
        self.worker.resultResiduals.connect(self.setValRes)
        self.worker.resultResPercent.connect(self.setValResPercent)
        
        self.worker.resultEps.connect(self.setValEps)
        self.worker.resultTemp.connect(self.setValTemp)
        self.worker.resultnbMeas.connect(self.setValNbMeas)
        
        
    def stopContMode(self):
        """ stops the continuous mode"""
        # we press the stop button --> running = False
        self.worker.running = False
        
        self.ui.startButtonS.setHidden(False)
        self.ui.stopButton.setHidden(True)
        self.ui.startContButtonS.setHidden(False)
        
        #Separating json in dataframes to write it in csv
        #Might be possible to optimize this part
        print(window.sampleFolder + "continuous_sample_values.json")

        """dfsample = pd.read_json(window.sampleFolder + "continuous_sample_values.json")
        contTimeList = pd.DataFrame(dfsample['contTimeList'].tolist()) 
        contTempListCel = pd.DataFrame(dfsample['contTempListCel'].tolist())
        contEpsList = pd.DataFrame(dfsample['contEpsList'].tolist())
        contPower = pd.DataFrame(dfsample['contPower'].tolist())
        contLuminanceSample = pd.DataFrame(dfsample['contLuminanceSample'].tolist())
        contLuminanceFit = pd.DataFrame(dfsample['contLuminanceFit'].tolist())
        contResiduals = pd.DataFrame(dfsample['contResiduals'].tolist())
        contResidualsPercent = pd.DataFrame(dfsample['contResidualsPercent'].tolist())

        csvdfsample = pd.concat([contTimeList,contTempListCel,contEpsList,contPower,
                                  contLuminanceSample,contLuminanceFit,contResiduals,
                                  contResidualsPercent], axis=1) #merging dataframes"""

        self.p = len(self.wavelengths)
        fieldnames = ['contTimeList', 'contTempListCel', 'contEpsList'] #Csv header
        for i in range(self.p): #creating the header
            fieldnames.append('Power'+str(i+1))
        for i in range(self.p): #Must use this much loops to have everything separated
            fieldnames.append('LuminanceSample'+str(i+1))
        for i in range(self.p):
            fieldnames.append('LuminanceFit'+str(i+1))
        for i in range(self.p):
            fieldnames.append('Residuals'+str(i+1))
        for i in range(self.p):
            fieldnames.append('Residuals(%)'+str(i+1))
        #converting to csv
        """csvdfsample.to_csv(window.sampleFolder + "continuous_sample_values.csv",index=False,header=fieldnames,sep=';') """
        
    
    def drawWvlgthLum(self,wavelength, lum_spl, lum_calib, temperatureListK, initGuessK):
        a = np.array(lum_calib)

        """Plots the luminance curves as a function of temperatures (in K) and wavelengths"""
        print("- - - - - - - - - - - - - - ")
        n = len(temperatureListK)
        self.plotWidgetUp.canvas.ax.scatter(wavelength, lum_spl, label='sample data')#Plotting the sample data
        plt.close()
        transposed = a.transpose()       
        for i in range(n): #For each temperature            
            #initGuessK is the initial guesses array for the calibration curves. We have to put the parameters temperatures to have an ideal fit
            fit = curve_fit(plck.planck, wavelength, transposed[i], initGuessK) #Fitting the data with the planck function (x->wavelengths, y->luminance)
            fit_results, cov = fit #cov is the covariance matrix
            fit_T, fit_epsilon = fit_results
            x = np.linspace(0.95, 1.65)#Getting a set of data to draw the model curve
            self.plotWidgetUp.canvas.ax.scatter(wavelength, transposed[i], color=color_list[i], marker='.')#Plotting the data
            self.plotWidgetUp.canvas.ax.plot(x, plck.planck(x, fit_T, fit_epsilon), color=color_list[i], label =f"T{i}={round(fit_T,2)}K, e={fit_epsilon:.3e}")
        
        self.plotWidgetUp.canvas.ax.set_title("Luminance = f(Wavelength)")    
        self.plotWidgetUp.canvas.ax.set_xlabel("Wavelength [µm]")
        self.plotWidgetUp.canvas.ax.set_ylabel("Luminance [W.m-2.str-1.µm-1]")
        self.plotWidgetUp.canvas.ax.legend()
        self.plotWidgetUp.canvas.draw()
        print("- - - - - - - - - - - - - - ")
        
        
    def curveFit(self, wavelength, luminance, initGuess, tempLim, epsLim, save_results_to):
        """Fits the sample curve and tries to guess its temperature and emissivity (epsilon)"""
        param_bounds = ((tempLim[0],epsLim[0]),(tempLim[1],epsLim[1]))#Here, bounds signifies that fit_T and fit_epsilon will be between the limits set in parameters

        try :
            if window.bounds and window.sigma:
                print("sigma and bounds")
                fit_results, cov = curve_fit(f=plck.planck, xdata=wavelength, ydata=luminance, p0=initGuess, sigma=luminance, bounds=param_bounds)
            
            elif window.bounds and not window.sigma: #bounds but no sigma
                print("bounds no sigma")
                fit_results, cov = curve_fit(f=plck.planck, xdata=wavelength, ydata=luminance, p0=initGuess, bounds=param_bounds)
            
            elif window.sigma and not window.bounds: #sigma but no bounds
                print("sigma no bounds")
                fit_results, cov = curve_fit(f=plck.planck, xdata=wavelength, ydata=luminance, p0=initGuess, sigma=luminance)
            
            else: #no sigma no bounds
                print("no sigma no bounds")
                fit_results, cov = curve_fit(f=plck.planck, xdata=wavelength, ydata=luminance, p0=initGuess) #Fitting the data with the planck function (x->wavelengths, y->luminance)
        
            fit_TK, fit_epsilon = fit_results
        except RuntimeError:#If there are errors when we fit (might be beacause the T° is too low)
            print("The least-square minimization failed")
            pass
        except ValueError:
            print("Xdata or Ydata may contains wrong values, or incompatible options are used")
            pass
        #cov is the covariance matrix, fit_results is the temperature and epsilon
        
        x = np.linspace(0.95, 1.65)#Getting a set of data to draw the model curve
        #Plotting the fit curve with the estimated parameters (Temperature and epsilon)
        self.plotWidgetUp.canvas.ax.plot(x, plck.planck(x, fit_TK, fit_epsilon), color= '#17becf', label=f"model:T={round(fit_TK,2)}K, e={fit_epsilon:.3e}")
                
        fit_TCel = plck.kelvinToCelsius(fit_TK)#Getting the fitted temperatures (displayed and real)
        fit_Tdisp = (fit_TCel/calib_temp_a)-calib_temp_b
        print("fitT : ",format(fit_TK,'.3f'),'K <=>', format(fit_TCel,'.3f'), 'Cel (real T), displayed T=',
              format(fit_Tdisp,'.3f'),' \nfit_e:',format(fit_epsilon,'.5f'))
        
        return fit_Tdisp, fit_epsilon, fit_TK, fit_TCel        
    
    
    def tempEpsEvolution(self,contTimeList,contTempList,contEpsList):
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        self.plotWidgetDown.canvas.fig.suptitle('Evolution of temperature [°C] and emissivity through time [s]')
        self.plotWidgetDown.canvas.axs[0].scatter(contTimeList, contTempList, label="Temperature [°C]")
        self.plotWidgetDown.canvas.axs[1].scatter(contTimeList, contEpsList, label="Emissivity")
        self.plotWidgetDown.canvas.axs[0].set_xlabel("Time [s]")
        
        # Hide x labels and tick labels for all but bottom plot
        for ax in self.plotWidgetDown.canvas.axs:
            ax.label_outer()
        plt.close()
        self.plotWidgetDown.canvas.draw()
        
        
    def clearplotWidgetUp(self):
        self.plotWidgetUp.canvas.ax.clear()
        
        
    def clearplotWidgetDown(self):
        self.plotWidgetDown.canvas.ax.clear()
    
    """Partie du programme Acquisition rapide de la puissance des photodiodes"""

    def NbrePts_changed(self, text):
        print(f"Nbre de pts changed...{text}")
        self.par = self.openJson("parameters") # Ouverture du fichier Json "parameters"
        self.nbre_pts = text
        self.par["nbre_pts"] = text
        self.saveJson(self.par,"parameters") #Sauvegarde dans le fichier Json "parameters"

    def AverageTime_changed(self, text):
        print(f"Temps d'intégration changed...{text}")
        self.par = self.openJson("parameters")
        self.Aver_Time = text
        self.par["Ar_Time"] = text
        self.saveJson(self.par,"parameters")

    def Unit_changed(self, text):

        """Update la valeur de "List_Unit 
        et sauvegarde dans le fichier parameters.json"""

        print(f"Unité changed...{text}")
        self.par = self.openJson("parameters")
        self.unit = text
        self.par["List_Unit"] = text
        self.saveJson(self.par,"parameters")

    def Delay_Read_Buffer_changed(self, text):
        print(f"Délai buffer dataKeysight changed...{text}")
        self.par = self.openJson("parameters")
        self.Delay_R_Buf = text
        self.par["Delay_Read_Buf"] = text
        self.saveJson(self.par,"parameters")
    
class ThreadMeasure(QThread):
    resultPow = pyqtSignal(str) #Creating signals to communicate with the GUI through the thread
    resultLum = pyqtSignal(str)
    resultFitLum = pyqtSignal(str)
    resultResiduals = pyqtSignal(str)
    resultResPercent = pyqtSignal(str)
    resultEps = pyqtSignal(str)
    resultTemp = pyqtSignal(str)
    resultnbMeas = pyqtSignal(str)
    
    def __init__(self):
        print("init just once ?")
        QThread.__init__(self)
        self.running = False #Helps to exit the thread    
        """Defining the variables for measurement"""
        self.par = window.openJson("parameters")
        self.calibration_data = window.openJson("calibration_data")
        
        self.temperatureListK = self.par["temperatureListK"]
        self.temperatureListCel = self.par["temperature_ListCel"]
        self.n = len(self.temperatureListK)
        self.p = len(self.par["wavelengths"]) # p is the number of wavelengths
        self.luminance_sample = [0 for j in range (self.p)]
        self.returnedpower = [0 for j in range(self.p)]
        self.returnedlum = [0 for j in range(self.p)] #Useless here as we will find it later using the nonlinear regression model and its parameters A,B&C. It helps using the same function
                
        #Getting the A,B,C values from the files        
        self.Alist = self.calibration_data["A"]
        self.Blist = self.calibration_data["B"]
        self.Clist = self.calibration_data["C"]  
        self.lum_calib = self.calibration_data["lum_calib"]  
    
        #Getting the values from the files for the limits used in the curve fit method
        self.tempLim = self.par["temperatureLimits"]
        self.epsLim = self.par["epsilonLimits"]
        self.initGuess = self.par["init_guess"]        
        self.initGuessK = [plck.celsiusToKelvin(self.initGuess[0]), self.initGuess[1]] #Converting the Celsius to K
        self.tempLimK = [plck.celsiusToKelvin(t) for t in self.tempLim]
        self.delay = self.par["delay"]

        self.nbre_pts = self.par["nbre_pts"]
        self.Aver_Time = self.par["Ar_Time"]
        self.unit = self.par["List_Unit"]
        self.Delay_R_Buf = self.par["Delay_Read_Buf"]
        
        self.contTimeList = []
        self.contEpsList = []
        self.contTempList = []
        
        self.nbMeasure = 0
        self.display = True
        
    
    def sampleMain(self):
        """Starts a parallel thread to run a measurement while modifying the GUI (Graphical User Interface)"""
        self.startingtime = time.time()
        #Stocking the values of wavelength and power        
        
        #Run the main function which reads the power at each photodiode
        self.power_sample, self.all_temp_values = app.run(window.N7745C, self.Delay_R_Buf, 'sample', self.temperatureListK, self.temperatureListK[0],self.returnedpower, self.returnedlum, window.wavelengths)
        print("power :",self.power_sample)
        print("all_temp_values :",self.all_temp_values)
        #logger.info(f"all_power :{self.all_temp_values}")

        for line in range(self.p):#For each photodiode
            #Calculating the luminance of the sample from its measured power and stocked A and B values
            self.luminance_sample[line] = pow((self.power_sample[line] - float(self.Blist[line])) / float(self.Alist[line]), 1/float(self.Clist[line]))
            if np.imag(self.luminance_sample[line])!=0 :#If the luminance is an imaginary complex, we set it by default at 0
               self.luminance_sample[line] = 0
               print("imaginary number")
            self.returnedlum[line]=float(format(self.luminance_sample[line],'.3e'))
    
    
    def fitting(self):
        print("fitting")      
        window.clearplotWidgetUp()
        window.clearplotWidgetDown()
        #Fitting the curve to find the temperature of the sample, fit_Tdisp is the fitted displayed T and fit_TK is the fitted T(Cel) in K
        if not self.running:
            window.drawWvlgthLum(window.wavelengths, self.luminance_sample, self.lum_calib, self.temperatureListK, self.initGuessK)
            print("plotting")
        else:
            if self.nbMeasure%10==0 or self.delay!=0: #Every 10 measures we display the graphs
                window.tempEpsEvolution(self.contTimeList, self.contTempList, self.contEpsList)
        self.fit_Tdisp, self.fit_epsilon, self.fit_TK, self.fit_T = window.curveFit(window.wavelengths, self.luminance_sample, self.initGuessK, self.tempLimK, self.epsLim, window.cdir) 
        self.initGuessK = [self.fit_TK,self.fit_epsilon] #Trying to fit faster by starting at the latest T° and e
        print("init guess : ",self.initGuessK)
        #Displaying the residuals
        self.residuals, self.luminance_fit, self.residualspercent = plot.drawResiduals(window.wavelengths, self.luminance_sample, self.fit_TK, self.fit_epsilon, self.display, window.cdir) 
       
        self.power_sample_reduced = []
    
        for i in range(len(self.power_sample)):
            self.power_sample_reduced.append(float(f"{self.power_sample[i]:.3e}"))
            
        
    """def saveOneValue(self):
        #Adding the values to the lists
        self.sample_values = {}
        self.sample_values["power_sample"] = self.power_sample
        self.sample_values["lum_sample"] = self.luminance_sample
        self.sample_values["lum_fit"] = self.luminance_fit
        self.sample_values["residuals"] = self.residuals
        self.sample_values["residuals_%"] = self.residualspercent        
        self.sample_values["temperature"] = self.fit_T
        self.sample_values["epsilon"] = self.fit_epsilon 
        self.sample_values["timeSample"] = window.t0
        self.sample_values["all_power_sample"] = self.all_temp_values

        #Saving the values into the file         
        
        window.saveJson(self.sample_values, "sample_values" + window.t0, 'w+')
        dfOnesample = pd.read_json(window.cdir + "sample_values" + window.t0 + ".json") #Separating json in dataframes
        fieldnames = ['power_sample', 'lum_sample', 'lum_fit','residuals','residuals_%','temperature','epsilon','timeSample','all_power_sample'] # csv header
        
        dfOnesample.to_csv(window.cdir + "sample_values" + window.t0 + ".csv",index=False,header=fieldnames,sep=';') #converting to csv"""
    def saveOneValue(self):
        # Adding the values to the lists
        self.sample_values = {}
        self.sample_values["power_sample"] = self.power_sample
        self.sample_values["lum_sample"] = self.luminance_sample
        self.sample_values["lum_fit"] = self.luminance_fit
        self.sample_values["residuals"] = self.residuals
        self.sample_values["residuals_%"] = self.residualspercent        
        self.sample_values["temperature"] = self.fit_T
        self.sample_values["epsilon"] = self.fit_epsilon 
        self.sample_values["timeSample"] = window.t0
        self.sample_values["all_power_sample"] = self.all_temp_values

        # Convert self.all_temp_values to a DataFrame for better handling
        all_temp_values_df = pd.DataFrame(self.all_temp_values).transpose()
        all_temp_values_df.columns = [f"all_power_sample_{i+1}" for i in range(all_temp_values_df.shape[1])]

        # Save the main values into a JSON file
        window.saveJson(self.sample_values, "sample_values" + window.t0, 'w+')

        # Load the saved JSON for consistency
        dfOnesample = pd.read_json(window.cdir + "sample_values" + window.t0 + ".json")  # Separating JSON into a DataFrame

        # Merge all_temp_values_df with the other data
        dfOnesample = pd.concat([dfOnesample, all_temp_values_df], axis=1)

        # Generate fieldnames dynamically
        fieldnames = list(self.sample_values.keys()) + list(all_temp_values_df.columns)

        # Save as CSV
        dfOnesample.to_csv(
            window.cdir + "sample_values" + window.t0 + ".csv",
            index=False,
            header=fieldnames,
            sep=';'
        )


        
    def saveContValues(self):
        
        self.sample_values = window.openJson(window.sampleFolder + "continuous_sample_values")
        #Saving the values into the file
        self.sample_values["nbMeasure"]=self.nbMeasure
        self.sample_values["startingTime"]=window.t0 
        self.sample_values["contTimeList"].append(self.startingtime-window.tinit)
        self.sample_values["contTempListCel"].append(self.fit_T) 
        self.sample_values["contEpsList"].append(self.fit_epsilon)
        self.sample_values["contPower"].append(self.power_sample)
        self.sample_values["contLuminanceSample"].append(self.luminance_sample)
        self.sample_values["contLuminanceFit"].append(self.luminance_fit)
        self.sample_values["contResiduals"].append(self.residuals)
        self.sample_values["contResidualsPercent"].append(self.residualspercent)
        
    
        window.saveJson(self.sample_values, window.sampleFolder + "continuous_sample_values", 'w+')
        
        
        self.contTimeList = self.sample_values["contTimeList"]
        self.contEpsList = self.sample_values["contEpsList"]
        self.contTempList = self.sample_values["contTempListCel"]
       
        
    def run(self):
        """Last part of the sample measurement function where we call the thread and keep the measurement loop"""
        self.sampleMain()
        self.sample_values = {"contTimeList":[],"contEpsList":[],"contTempListCel":[],
                              "contPower":[],"contLuminanceSample":[],"contLuminanceFit":[],
                              "contResiduals":[],"contResidualsPercent":[]}
        window.saveJson(self.sample_values, window.sampleFolder + "continuous_sample_values", 'w+')
   
        if not self.running: #If this is a single measure
            self.fitting()            
            self.signalEmit()             
            print("nb measure:",self.nbMeasure)
            self.saveOneValue()
        
        while self.running: #If we haven't pressed the stop button, the measurement keeps going
            if self.delay!=0 or self.delay!=None: #If there is a delay
                QTest.qWait(self.delay*1000)
                self.continuousMeasure()
            else:
                self.continuousMeasure()
            
            
    def continuousMeasure(self):
        self.sampleMain()
        self.display=False
        self.fitting()            
        self.signalEmit()            
        print("nb measure:",self.nbMeasure)                
        self.saveContValues()
        self.AllMeasure()                
        self.nbMeasure += 1  
    
    def AllMeasure(self):

        file_index = 1
        while os.path.exists(f'all_temp_values_{file_index}.json'):
            file_index += 1
        
        # Créer un dictionnaire avec la structure souhaitée
        formatted_data = {}
        for i, sublist in enumerate(self.all_temp_values, 1):
            formatted_data[f'canal{i}'] = sublist
        
        with open(f'all_temp_values_{file_index}.json', 'w') as json_file:
            json.dump(formatted_data, json_file)
    
    def signalEmit(self):
        self.resultPow.emit(str(self.power_sample_reduced))
        self.resultLum.emit(str(self.returnedlum))
        self.resultFitLum.emit(str(self.luminance_fit))
        self.resultResiduals.emit(str(self.residuals))
        self.resultResPercent.emit(str(self.residualspercent))        
        self.resultTemp.emit(format(self.fit_T, '.1f'))
        self.resultEps.emit(format(self.fit_epsilon, '.4f'))
        self.resultnbMeas.emit(str(self.nbMeasure))
    

#Creating a window with the application
if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    window = Pyro() #Creating the GUI
    window.show()
    sys.exit(application.exec_())


"""Conversion : pyuic5 newpyro_v2.ui -o newpyro_v2.py"""