# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newpyro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pyro(object):
    def setupUi(self, Pyro):
        Pyro.setObjectName("Pyro")
        Pyro.resize(1969, 995)
        self.centralwidget = QtWidgets.QWidget(Pyro)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 2000, 995))
        self.tabWidget.setObjectName("tabWidget")
        self.Calibration = QtWidgets.QWidget()
        self.Calibration.setAutoFillBackground(False)
        self.Calibration.setObjectName("Calibration")
        self.gridLayoutWidget = QtWidgets.QWidget(self.Calibration)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 1921, 961))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.cal_graphs = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.cal_graphs.setEnabled(True)
        self.cal_graphs.setStyleSheet("background : rgba(0,0,0,100);\n"
"color: rgb(255,255,255)")
        self.cal_graphs.setObjectName("cal_graphs")
        self.labelgraphUp = QtWidgets.QLabel(self.cal_graphs)
        self.labelgraphUp.setGeometry(QtCore.QRect(70, 30, 811, 451))
        self.labelgraphUp.setText("")
        self.labelgraphUp.setObjectName("labelgraphUp")
        self.widget = QtWidgets.QWidget(self.cal_graphs)
        self.widget.setGeometry(QtCore.QRect(70, 490, 811, 451))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.cal_graphs, 0, 1, 2, 1)
        self.cal_parameters = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.cal_parameters.setEnabled(True)
        self.cal_parameters.setAcceptDrops(False)
        self.cal_parameters.setAutoFillBackground(False)
        self.cal_parameters.setStyleSheet("background : rgba(0,0,0,100);\n"
"color: rgb(255,255,255)")
        self.cal_parameters.setFlat(False)
        self.cal_parameters.setCheckable(False)
        self.cal_parameters.setObjectName("cal_parameters")
        self.chooseFolder = QtWidgets.QPushButton(self.cal_parameters)
        self.chooseFolder.setGeometry(QtCore.QRect(500, 40, 121, 30))
        self.chooseFolder.setCheckable(False)
        self.chooseFolder.setAutoExclusive(False)
        self.chooseFolder.setAutoDefault(False)
        self.chooseFolder.setDefault(True)
        self.chooseFolder.setFlat(True)
        self.chooseFolder.setObjectName("chooseFolder")
        self.labelTemp = QtWidgets.QLabel(self.cal_parameters)
        self.labelTemp.setEnabled(False)
        self.labelTemp.setGeometry(QtCore.QRect(40, 100, 141, 30))
        self.labelTemp.setStyleSheet("background : rgba(255,255,255,0)\n"
"")
        self.labelTemp.setLineWidth(0)
        self.labelTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTemp.setObjectName("labelTemp")
        self.temperature = QtWidgets.QLineEdit(self.cal_parameters)
        self.temperature.setGeometry(QtCore.QRect(180, 100, 280, 30))
        self.temperature.setMaximumSize(QtCore.QSize(280, 16777215))
        self.temperature.setStyleSheet("")
        self.temperature.setText("")
        self.temperature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperature.setObjectName("temperature")
        self.labelWv = QtWidgets.QLabel(self.cal_parameters)
        self.labelWv.setEnabled(True)
        self.labelWv.setGeometry(QtCore.QRect(40, 160, 131, 30))
        self.labelWv.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelWv.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWv.setObjectName("labelWv")
        self.wavelength = QtWidgets.QLineEdit(self.cal_parameters)
        self.wavelength.setGeometry(QtCore.QRect(180, 160, 280, 30))
        self.wavelength.setMaximumSize(QtCore.QSize(280, 16777215))
        self.wavelength.setStyleSheet("")
        self.wavelength.setText("")
        self.wavelength.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wavelength.setObjectName("wavelength")
        self.labelAvg = QtWidgets.QLabel(self.cal_parameters)
        self.labelAvg.setEnabled(False)
        self.labelAvg.setGeometry(QtCore.QRect(470, 102, 151, 30))
        self.labelAvg.setStyleSheet("background : rgba(255,255,255,0)\n"
"")
        self.labelAvg.setLineWidth(0)
        self.labelAvg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAvg.setObjectName("labelAvg")
        self.avg_time = QtWidgets.QLineEdit(self.cal_parameters)
        self.avg_time.setGeometry(QtCore.QRect(630, 100, 280, 30))
        self.avg_time.setMaximumSize(QtCore.QSize(280, 16777215))
        self.avg_time.setStyleSheet("")
        self.avg_time.setText("")
        self.avg_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.avg_time.setObjectName("avg_time")
        self.startButton = QtWidgets.QPushButton(self.cal_parameters)
        self.startButton.setEnabled(True)
        self.startButton.setGeometry(QtCore.QRect(390, 250, 171, 30))
        self.startButton.setStyleSheet("")
        self.startButton.setCheckable(False)
        self.startButton.setAutoExclusive(False)
        self.startButton.setAutoDefault(False)
        self.startButton.setDefault(True)
        self.startButton.setFlat(True)
        self.startButton.setObjectName("startButton")
        self.labelVISA = QtWidgets.QLabel(self.cal_parameters)
        self.labelVISA.setGeometry(QtCore.QRect(30, 40, 141, 30))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelVISA.setFont(font)
        self.labelVISA.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelVISA.setTextFormat(QtCore.Qt.AutoText)
        self.labelVISA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVISA.setWordWrap(False)
        self.labelVISA.setObjectName("labelVISA")
        self.id_powermeter = QtWidgets.QComboBox(self.cal_parameters)
        self.id_powermeter.setGeometry(QtCore.QRect(180, 40, 280, 30))
        self.id_powermeter.setAutoFillBackground(False)
        self.id_powermeter.setStyleSheet("")
        self.id_powermeter.setEditable(False)
        self.id_powermeter.setCurrentText("")
        self.id_powermeter.setObjectName("id_powermeter")
        self.textTemperature = QtWidgets.QTextBrowser(self.cal_parameters)
        self.textTemperature.setGeometry(QtCore.QRect(350, 300, 251, 91))
        self.textTemperature.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textTemperature.setLineWrapColumnOrWidth(0)
        self.textTemperature.setObjectName("textTemperature")
        self.labelDir = QtWidgets.QLineEdit(self.cal_parameters)
        self.labelDir.setGeometry(QtCore.QRect(630, 40, 280, 30))
        self.labelDir.setObjectName("labelDir")
        self.okButton = QtWidgets.QPushButton(self.cal_parameters)
        self.okButton.setEnabled(False)
        self.okButton.setGeometry(QtCore.QRect(390, 420, 171, 30))
        self.okButton.setStyleSheet("")
        self.okButton.setCheckable(False)
        self.okButton.setAutoExclusive(False)
        self.okButton.setAutoDefault(False)
        self.okButton.setDefault(True)
        self.okButton.setFlat(True)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.cal_parameters, 0, 0, 1, 1)
        self.cal_values = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.cal_values.setStyleSheet("background : rgba(0,0,0,100);\n"
"color: rgb(255,255,255)")
        self.cal_values.setObjectName("cal_values")
        self.labelValPow = QtWidgets.QLabel(self.cal_values)
        self.labelValPow.setGeometry(QtCore.QRect(135, 290, 81, 131))
        self.labelValPow.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelValPow.setAlignment(QtCore.Qt.AlignCenter)
        self.labelValPow.setObjectName("labelValPow")
        self.labelvalLum = QtWidgets.QLabel(self.cal_values)
        self.labelvalLum.setGeometry(QtCore.QRect(100, 70, 161, 161))
        self.labelvalLum.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelvalLum.setAlignment(QtCore.Qt.AlignCenter)
        self.labelvalLum.setWordWrap(True)
        self.labelvalLum.setObjectName("labelvalLum")
        self.valLum = QtWidgets.QTextBrowser(self.cal_values)
        self.valLum.setGeometry(QtCore.QRect(260, 80, 471, 151))
        self.valLum.setObjectName("valLum")
        self.valPow = QtWidgets.QTextBrowser(self.cal_values)
        self.valPow.setGeometry(QtCore.QRect(260, 280, 471, 151))
        self.valPow.setObjectName("valPow")
        self.gridLayout.addWidget(self.cal_values, 1, 0, 1, 1)
        self.tabWidget.addTab(self.Calibration, "")
        self.Sample = QtWidgets.QWidget()
        self.Sample.setObjectName("Sample")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.Sample)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 1921, 961))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.leftLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout.setObjectName("leftLayout")
        self.Graphs = QtWidgets.QGroupBox(self.gridLayoutWidget_3)
        self.Graphs.setStyleSheet("background : rgba(0,0,0,100);\n"
"color: rgb(255,255,255)")
        self.Graphs.setObjectName("Graphs")
        self.widgetUp = QtWidgets.QWidget(self.Graphs)
        self.widgetUp.setGeometry(QtCore.QRect(70, 30, 811, 451))
        self.widgetUp.setObjectName("widgetUp")
        self.widgetDown = QtWidgets.QWidget(self.Graphs)
        self.widgetDown.setEnabled(False)
        self.widgetDown.setGeometry(QtCore.QRect(70, 490, 811, 451))
        self.widgetDown.setObjectName("widgetDown")
        self.leftLayout.addWidget(self.Graphs, 0, 1, 2, 1)
        self.Val = QtWidgets.QGroupBox(self.gridLayoutWidget_3)
        self.Val.setStyleSheet("background : rgba(0,0,0,100);\n"
"color: rgb(255,255,255)")
        self.Val.setObjectName("Val")
        self.labelActTemp = QtWidgets.QLabel(self.Val)
        self.labelActTemp.setEnabled(True)
        self.labelActTemp.setGeometry(QtCore.QRect(580, 240, 171, 30))
        self.labelActTemp.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelActTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelActTemp.setObjectName("labelActTemp")
        self.labelEm = QtWidgets.QLabel(self.Val)
        self.labelEm.setEnabled(False)
        self.labelEm.setGeometry(QtCore.QRect(635, 150, 81, 30))
        self.labelEm.setStyleSheet("background : rgba(255,255,255,0)\n"
"")
        self.labelEm.setLineWidth(0)
        self.labelEm.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEm.setObjectName("labelEm")
        self.labelvalPowS = QtWidgets.QLabel(self.Val)
        self.labelvalPowS.setGeometry(QtCore.QRect(62, 60, 81, 30))
        self.labelvalPowS.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelvalPowS.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelvalPowS.setAlignment(QtCore.Qt.AlignCenter)
        self.labelvalPowS.setObjectName("labelvalPowS")
        self.labelvalResP = QtWidgets.QLabel(self.Val)
        self.labelvalResP.setGeometry(QtCore.QRect(55, 410, 101, 41))
        self.labelvalResP.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelvalResP.setScaledContents(False)
        self.labelvalResP.setAlignment(QtCore.Qt.AlignCenter)
        self.labelvalResP.setWordWrap(True)
        self.labelvalResP.setObjectName("labelvalResP")
        self.valEps = QtWidgets.QTextBrowser(self.Val)
        self.valEps.setGeometry(QtCore.QRect(760, 140, 131, 50))
        self.valEps.setObjectName("valEps")
        self.valTemp = QtWidgets.QTextBrowser(self.Val)
        self.valTemp.setGeometry(QtCore.QRect(760, 230, 131, 50))
        self.valTemp.setObjectName("valTemp")
        self.valPowS = QtWidgets.QTextBrowser(self.Val)
        self.valPowS.setGeometry(QtCore.QRect(180, 50, 371, 50))
        self.valPowS.setObjectName("valPowS")
        self.valResidualsP = QtWidgets.QTextBrowser(self.Val)
        self.valResidualsP.setGeometry(QtCore.QRect(180, 410, 371, 50))
        self.valResidualsP.setObjectName("valResidualsP")
        self.labelNbMeasure = QtWidgets.QLabel(self.Val)
        self.labelNbMeasure.setEnabled(True)
        self.labelNbMeasure.setGeometry(QtCore.QRect(610, 330, 121, 30))
        self.labelNbMeasure.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelNbMeasure.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNbMeasure.setObjectName("labelNbMeasure")
        self.valNbMeasure = QtWidgets.QTextBrowser(self.Val)
        self.valNbMeasure.setGeometry(QtCore.QRect(760, 320, 131, 50))
        self.valNbMeasure.setObjectName("valNbMeasure")
        self.labelvalLum_2 = QtWidgets.QLabel(self.Val)
        self.labelvalLum_2.setGeometry(QtCore.QRect(20, 140, 151, 51))
        self.labelvalLum_2.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelvalLum_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelvalLum_2.setWordWrap(True)
        self.labelvalLum_2.setObjectName("labelvalLum_2")
        self.valLuminance = QtWidgets.QTextBrowser(self.Val)
        self.valLuminance.setGeometry(QtCore.QRect(180, 140, 371, 50))
        self.valLuminance.setObjectName("valLuminance")
        self.labelvalRes = QtWidgets.QLabel(self.Val)
        self.labelvalRes.setGeometry(QtCore.QRect(55, 320, 101, 41))
        self.labelvalRes.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelvalRes.setScaledContents(False)
        self.labelvalRes.setAlignment(QtCore.Qt.AlignCenter)
        self.labelvalRes.setWordWrap(True)
        self.labelvalRes.setObjectName("labelvalRes")
        self.valResiduals = QtWidgets.QTextBrowser(self.Val)
        self.valResiduals.setGeometry(QtCore.QRect(180, 320, 371, 50))
        self.valResiduals.setObjectName("valResiduals")
        self.labelvalFitLum = QtWidgets.QLabel(self.Val)
        self.labelvalFitLum.setGeometry(QtCore.QRect(20, 230, 151, 41))
        self.labelvalFitLum.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelvalFitLum.setScaledContents(False)
        self.labelvalFitLum.setAlignment(QtCore.Qt.AlignCenter)
        self.labelvalFitLum.setWordWrap(True)
        self.labelvalFitLum.setObjectName("labelvalFitLum")
        self.valFitLum = QtWidgets.QTextBrowser(self.Val)
        self.valFitLum.setGeometry(QtCore.QRect(180, 230, 371, 50))
        self.valFitLum.setObjectName("valFitLum")
        self.leftLayout.addWidget(self.Val, 1, 0, 1, 1)
        self.Param = QtWidgets.QGroupBox(self.gridLayoutWidget_3)
        self.Param.setEnabled(True)
        self.Param.setStyleSheet("background : rgba(0,0,0,100);\n"
"color: rgb(255,255,255)")
        self.Param.setObjectName("Param")
        self.labelAvgs = QtWidgets.QLabel(self.Param)
        self.labelAvgs.setEnabled(False)
        self.labelAvgs.setGeometry(QtCore.QRect(20, 110, 111, 61))
        self.labelAvgs.setStyleSheet("background : rgba(255,255,255,0)\n"
"")
        self.labelAvgs.setLineWidth(0)
        self.labelAvgs.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAvgs.setWordWrap(True)
        self.labelAvgs.setObjectName("labelAvgs")
        self.avg_timeS = QtWidgets.QLineEdit(self.Param)
        self.avg_timeS.setGeometry(QtCore.QRect(140, 120, 280, 30))
        self.avg_timeS.setMaximumSize(QtCore.QSize(300, 16777215))
        self.avg_timeS.setStyleSheet("")
        self.avg_timeS.setText("")
        self.avg_timeS.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.avg_timeS.setObjectName("avg_timeS")
        self.labelTempLim = QtWidgets.QLabel(self.Param)
        self.labelTempLim.setEnabled(True)
        self.labelTempLim.setGeometry(QtCore.QRect(30, 230, 101, 91))
        self.labelTempLim.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelTempLim.setScaledContents(False)
        self.labelTempLim.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTempLim.setWordWrap(True)
        self.labelTempLim.setObjectName("labelTempLim")
        self.temp_limit = QtWidgets.QLineEdit(self.Param)
        self.temp_limit.setGeometry(QtCore.QRect(140, 260, 280, 30))
        self.temp_limit.setMaximumSize(QtCore.QSize(280, 16777215))
        self.temp_limit.setStyleSheet("")
        self.temp_limit.setText("")
        self.temp_limit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temp_limit.setObjectName("temp_limit")
        self.labelEmlim = QtWidgets.QLabel(self.Param)
        self.labelEmlim.setEnabled(True)
        self.labelEmlim.setGeometry(QtCore.QRect(480, 260, 121, 30))
        self.labelEmlim.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelEmlim.setAutoFillBackground(False)
        self.labelEmlim.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelEmlim.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEmlim.setObjectName("labelEmlim")
        self.em_limit = QtWidgets.QLineEdit(self.Param)
        self.em_limit.setGeometry(QtCore.QRect(610, 260, 280, 30))
        self.em_limit.setMinimumSize(QtCore.QSize(280, 0))
        self.em_limit.setMaximumSize(QtCore.QSize(280, 16777215))
        self.em_limit.setStyleSheet("")
        self.em_limit.setText("")
        self.em_limit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.em_limit.setObjectName("em_limit")
        self.labelVISAs = QtWidgets.QLabel(self.Param)
        self.labelVISAs.setGeometry(QtCore.QRect(20, 40, 111, 30))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelVISAs.setFont(font)
        self.labelVISAs.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelVISAs.setTextFormat(QtCore.Qt.AutoText)
        self.labelVISAs.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVISAs.setWordWrap(True)
        self.labelVISAs.setObjectName("labelVISAs")
        self.id_powermeterS = QtWidgets.QComboBox(self.Param)
        self.id_powermeterS.setGeometry(QtCore.QRect(140, 40, 281, 30))
        self.id_powermeterS.setAutoFillBackground(False)
        self.id_powermeterS.setStyleSheet("")
        self.id_powermeterS.setEditable(False)
        self.id_powermeterS.setCurrentText("")
        self.id_powermeterS.setObjectName("id_powermeterS")
        self.chooseFolderS = QtWidgets.QPushButton(self.Param)
        self.chooseFolderS.setGeometry(QtCore.QRect(480, 40, 121, 30))
        self.chooseFolderS.setCheckable(False)
        self.chooseFolderS.setAutoExclusive(False)
        self.chooseFolderS.setAutoDefault(False)
        self.chooseFolderS.setDefault(True)
        self.chooseFolderS.setFlat(True)
        self.chooseFolderS.setObjectName("chooseFolderS")
        self.labelDirS = QtWidgets.QLineEdit(self.Param)
        self.labelDirS.setGeometry(QtCore.QRect(610, 40, 280, 30))
        self.labelDirS.setObjectName("labelDirS")
        self.startButtonS = QtWidgets.QPushButton(self.Param)
        self.startButtonS.setEnabled(True)
        self.startButtonS.setGeometry(QtCore.QRect(160, 370, 191, 81))
        self.startButtonS.setStyleSheet("")
        self.startButtonS.setCheckable(False)
        self.startButtonS.setAutoExclusive(False)
        self.startButtonS.setDefault(True)
        self.startButtonS.setFlat(True)
        self.startButtonS.setObjectName("startButtonS")
        self.stopButton = QtWidgets.QPushButton(self.Param)
        self.stopButton.setEnabled(False)
        self.stopButton.setGeometry(QtCore.QRect(380, 370, 191, 81))
        self.stopButton.setStyleSheet("")
        self.stopButton.setCheckable(False)
        self.stopButton.setAutoExclusive(False)
        self.stopButton.setAutoDefault(False)
        self.stopButton.setDefault(True)
        self.stopButton.setFlat(True)
        self.stopButton.setObjectName("stopButton")
        self.startContButtonS = QtWidgets.QPushButton(self.Param)
        self.startContButtonS.setEnabled(True)
        self.startContButtonS.setGeometry(QtCore.QRect(600, 370, 191, 81))
        self.startContButtonS.setStyleSheet("")
        self.startContButtonS.setCheckable(False)
        self.startContButtonS.setAutoExclusive(False)
        self.startContButtonS.setDefault(True)
        self.startContButtonS.setFlat(True)
        self.startContButtonS.setObjectName("startContButtonS")
        self.checkBoxBounds = QtWidgets.QCheckBox(self.Param)
        self.checkBoxBounds.setGeometry(QtCore.QRect(610, 190, 281, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.checkBoxBounds.setFont(font)
        self.checkBoxBounds.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.checkBoxBounds.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBoxBounds.setChecked(False)
        self.checkBoxBounds.setObjectName("checkBoxBounds")
        self.init_guess = QtWidgets.QLineEdit(self.Param)
        self.init_guess.setGeometry(QtCore.QRect(610, 120, 280, 30))
        self.init_guess.setMaximumSize(QtCore.QSize(300, 16777215))
        self.init_guess.setStyleSheet("")
        self.init_guess.setText("")
        self.init_guess.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.init_guess.setObjectName("init_guess")
        self.labelinit_guess = QtWidgets.QLabel(self.Param)
        self.labelinit_guess.setEnabled(False)
        self.labelinit_guess.setGeometry(QtCore.QRect(480, 120, 121, 30))
        self.labelinit_guess.setStyleSheet("background : rgba(255,255,255,0)\n"
"")
        self.labelinit_guess.setLineWidth(0)
        self.labelinit_guess.setAlignment(QtCore.Qt.AlignCenter)
        self.labelinit_guess.setObjectName("labelinit_guess")
        self.checkBoxSigma = QtWidgets.QCheckBox(self.Param)
        self.checkBoxSigma.setGeometry(QtCore.QRect(140, 190, 281, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.checkBoxSigma.setFont(font)
        self.checkBoxSigma.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.checkBoxSigma.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBoxSigma.setChecked(False)
        self.checkBoxSigma.setObjectName("checkBoxSigma")
        self.labelDelay = QtWidgets.QLabel(self.Param)
        self.labelDelay.setEnabled(True)
        self.labelDelay.setGeometry(QtCore.QRect(835, 380, 71, 21))
        self.labelDelay.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelDelay.setAutoFillBackground(False)
        self.labelDelay.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelDelay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDelay.setObjectName("labelDelay")
        self.delay = QtWidgets.QLineEdit(self.Param)
        self.delay.setGeometry(QtCore.QRect(835, 410, 71, 30))
        self.delay.setMinimumSize(QtCore.QSize(0, 0))
        self.delay.setMaximumSize(QtCore.QSize(280, 16777215))
        self.delay.setStyleSheet("")
        self.delay.setText("")
        self.delay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.delay.setObjectName("delay")
        self.leftLayout.addWidget(self.Param, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Sample, "")
        Pyro.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pyro)
        self.tabWidget.setCurrentIndex(1)
        self.checkBoxBounds.clicked['bool'].connect(self.temp_limit.setVisible)
        self.checkBoxBounds.clicked['bool'].connect(self.labelTempLim.setVisible)
        self.checkBoxBounds.clicked['bool'].connect(self.em_limit.setVisible)
        self.checkBoxBounds.clicked['bool'].connect(self.labelEmlim.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Pyro)

    def retranslateUi(self, Pyro):
        _translate = QtCore.QCoreApplication.translate
        Pyro.setWindowTitle(_translate("Pyro", "MainWindow"))
        self.cal_graphs.setTitle(_translate("Pyro", "Graphs"))
        self.cal_parameters.setTitle(_translate("Pyro", "Parameters"))
        self.chooseFolder.setText(_translate("Pyro", "Choose folder"))
        self.labelTemp.setText(_translate("Pyro", "Temperatures [°C]"))
        self.temperature.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[T1,...,Ti,...,Tn] - Temperatures of calibration</span></p></body></html>"))
        self.labelWv.setText(_translate("Pyro", "Wavelengths [µm]"))
        self.wavelength.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[w1,...,wj,...,wn]</span></p></body></html>"))
        self.labelAvg.setText(_translate("Pyro", "Averaging time [ms]"))
        self.avg_time.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[A1,...,Aj,...,Ap]</span></p></body></html>"))
        self.avg_time.setWhatsThis(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[A1,A2,A3,A4]</span></p></body></html>"))
        self.startButton.setText(_translate("Pyro", "Start"))
        self.labelVISA.setText(_translate("Pyro", "Power Meter VISA"))
        self.id_powermeter.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Instrument adress</span></p></body></html>"))
        self.textTemperature.setHtml(_translate("Pyro", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt; vertical-align:middle;\">Press Start when ready to measure</span></p></body></html>"))
        self.okButton.setText(_translate("Pyro", "OK"))
        self.cal_values.setTitle(_translate("Pyro", "Values"))
        self.labelValPow.setText(_translate("Pyro", "Power [W]"))
        self.labelvalLum.setText(_translate("Pyro", "Luminance [W.m-2.µm-1.str-1]"))
        self.valLum.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Luminance with Planck\'s law (emissivity = 1 ; T +/- correction of the blackbody, see blackbody_calibration.py)</span></p></body></html>"))
        self.valPow.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Power received by the photodiodes</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Calibration), _translate("Pyro", "Calibration"))
        self.Graphs.setTitle(_translate("Pyro", "Graphs"))
        self.Val.setTitle(_translate("Pyro", "Values"))
        self.labelActTemp.setText(_translate("Pyro", "Actual temperature [°C]"))
        self.labelEm.setText(_translate("Pyro", "Emissivity"))
        self.labelvalPowS.setText(_translate("Pyro", "Power [W]"))
        self.labelvalResP.setText(_translate("Pyro", "Residuals [% luminance]"))
        self.valEps.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Fitted emissivity</span></p></body></html>"))
        self.valEps.setWhatsThis(_translate("Pyro", "Fitted emissivity"))
        self.valTemp.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Fitted temperature</span></p></body></html>"))
        self.valTemp.setWhatsThis(_translate("Pyro", "Fitted temperature"))
        self.valPowS.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Power received by the photodiodes</span></p></body></html>"))
        self.valPowS.setWhatsThis(_translate("Pyro", "Power received by the photodiodes"))
        self.valResidualsP.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Measured luminance - fitted luminance (using Planck\'s law with fitted T and E) in %</span></p></body></html>"))
        self.valResidualsP.setWhatsThis(_translate("Pyro", "Measured luminance - fitted luminance (using Planck\'s law with fitted T and E)"))
        self.labelNbMeasure.setText(_translate("Pyro", "Times measured"))
        self.labelvalLum_2.setText(_translate("Pyro", "Measured luminance [W.m-2.µm-1.str-1]"))
        self.valLuminance.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Measured luminance using the A,B &amp; C calibration coefficients </span></p></body></html>"))
        self.valLuminance.setWhatsThis(_translate("Pyro", "Measured luminance with the calibration coefficients"))
        self.labelvalRes.setText(_translate("Pyro", "Residuals [luminance]"))
        self.valResiduals.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Measured luminance - fitted luminance (using Planck\'s law with fitted T and E)</span></p></body></html>"))
        self.valResiduals.setWhatsThis(_translate("Pyro", "Measured luminance - fitted luminance (using Planck\'s law with fitted T and E)"))
        self.labelvalFitLum.setText(_translate("Pyro", "Fitted luminance [W.m-2.µm-1.str-1]"))
        self.valFitLum.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Fitted luminance (using Planck\'s law with fitted T and E)</span></p></body></html>"))
        self.valFitLum.setWhatsThis(_translate("Pyro", "Measured luminance - fitted luminance (using Planck\'s law with fitted T and E)"))
        self.Param.setTitle(_translate("Pyro", "Parameters"))
        self.labelAvgs.setText(_translate("Pyro", "Averaging time [ms]"))
        self.avg_timeS.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[A1,...,Aj,...,Ap]</span></p></body></html>"))
        self.labelTempLim.setText(_translate("Pyro", "Temperature limits [°C]"))
        self.temp_limit.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[Tmin, Tmax] bounds for the sample curve_fit function</span></p></body></html>"))
        self.temp_limit.setWhatsThis(_translate("Pyro", "[Tmin, Tmax] bounds for the sample curve_fit function"))
        self.labelEmlim.setText(_translate("Pyro", "Emissivity limits"))
        self.em_limit.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[Emin, Emax] bounds for the sample curve_fit function</span></p></body></html>"))
        self.em_limit.setWhatsThis(_translate("Pyro", "[Emin, Emax] bounds for the sample curve_fit function"))
        self.labelVISAs.setText(_translate("Pyro", "Power Meter VISA"))
        self.id_powermeterS.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Instrument adress</span></p></body></html>"))
        self.chooseFolderS.setText(_translate("Pyro", "Choose folder"))
        self.labelDirS.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Folder where the sample values, parameters and calibration values will be saved</span></p></body></html>"))
        self.startButtonS.setText(_translate("Pyro", "Start one measure"))
        self.stopButton.setText(_translate("Pyro", "Stop"))
        self.startContButtonS.setText(_translate("Pyro", "Start Continuous mode"))
        self.checkBoxBounds.setText(_translate("Pyro", "Add ε and T° bounds when fitting"))
        self.init_guess.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[Tguess, Eguess] - Temperature (°C) and Emissivity at which the fit will start</span></p><p><span style=\" color:#aa55ff;\">If the fit cannot be made, try to lower the temperature </span></p></body></html>"))
        self.labelinit_guess.setText(_translate("Pyro", "Initial Guesses"))
        self.checkBoxSigma.setText(_translate("Pyro", "Add sigma = (1 / y²) when fitting"))
        self.labelDelay.setText(_translate("Pyro", "Delay [s]"))
        self.delay.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[Emin, Emax] bounds for the sample curve_fit function</span></p></body></html>"))
        self.delay.setWhatsThis(_translate("Pyro", "[Emin, Emax] bounds for the sample curve_fit function"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sample), _translate("Pyro", "Sample"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pyro = QtWidgets.QMainWindow()
    ui = Ui_Pyro()
    ui.setupUi(Pyro)
    Pyro.show()
    sys.exit(app.exec_())
