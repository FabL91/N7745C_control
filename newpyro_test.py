# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newpyro_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pyro(object):
    def setupUi(self, Pyro):
        Pyro.setObjectName("Pyro")
        Pyro.resize(1415, 971)
        self.centralwidget = QtWidgets.QWidget(Pyro)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 1371, 931))
        self.tabWidget.setObjectName("tabWidget")
        self.Calibration = QtWidgets.QWidget()
        self.Calibration.setAutoFillBackground(False)
        self.Calibration.setObjectName("Calibration")
        self.widget = QtWidgets.QWidget(self.Calibration)
        self.widget.setGeometry(QtCore.QRect(570, 440, 731, 431))
        self.widget.setAutoFillBackground(True)
        self.widget.setStyleSheet("background-color: rgb(109,109,109);")
        self.widget.setObjectName("widget")
        self.labelgraphUp = QtWidgets.QLabel(self.Calibration)
        self.labelgraphUp.setGeometry(QtCore.QRect(560, 10, 731, 401))
        self.labelgraphUp.setAutoFillBackground(True)
        self.labelgraphUp.setStyleSheet("background-color: rgb(109, 109, 109);")
        self.labelgraphUp.setText("")
        self.labelgraphUp.setObjectName("labelgraphUp")
        self.cal_parameters = QtWidgets.QGroupBox(self.Calibration)
        self.cal_parameters.setEnabled(True)
        self.cal_parameters.setGeometry(QtCore.QRect(10, 10, 541, 401))
        self.cal_parameters.setAcceptDrops(False)
        self.cal_parameters.setAutoFillBackground(False)
        self.cal_parameters.setStyleSheet("background : rgba(0,0,0,100);\n"
"color: rgb(255,255,255)")
        self.cal_parameters.setFlat(False)
        self.cal_parameters.setCheckable(False)
        self.cal_parameters.setObjectName("cal_parameters")
        self.layoutWidget = QtWidgets.QWidget(self.cal_parameters)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 233, 78))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelVISA = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelVISA.setFont(font)
        self.labelVISA.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelVISA.setTextFormat(QtCore.Qt.PlainText)
        self.labelVISA.setWordWrap(False)
        self.labelVISA.setObjectName("labelVISA")
        self.horizontalLayout.addWidget(self.labelVISA)
        self.id_powermeter = QtWidgets.QComboBox(self.layoutWidget)
        self.id_powermeter.setAutoFillBackground(False)
        self.id_powermeter.setStyleSheet("")
        self.id_powermeter.setEditable(False)
        self.id_powermeter.setCurrentText("")
        self.id_powermeter.setObjectName("id_powermeter")
        self.horizontalLayout.addWidget(self.id_powermeter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelTemp = QtWidgets.QLabel(self.layoutWidget)
        self.labelTemp.setEnabled(False)
        self.labelTemp.setStyleSheet("background : rgba(255,255,255,0)\n"
"")
        self.labelTemp.setLineWidth(0)
        self.labelTemp.setObjectName("labelTemp")
        self.horizontalLayout_2.addWidget(self.labelTemp)
        self.temperature = QtWidgets.QLineEdit(self.layoutWidget)
        self.temperature.setMaximumSize(QtCore.QSize(280, 16777215))
        self.temperature.setStyleSheet("")
        self.temperature.setText("")
        self.temperature.setObjectName("temperature")
        self.horizontalLayout_2.addWidget(self.temperature)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelWv = QtWidgets.QLabel(self.layoutWidget)
        self.labelWv.setEnabled(True)
        self.labelWv.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelWv.setObjectName("labelWv")
        self.horizontalLayout_3.addWidget(self.labelWv)
        self.wavelength = QtWidgets.QLineEdit(self.layoutWidget)
        self.wavelength.setMaximumSize(QtCore.QSize(280, 16777215))
        self.wavelength.setStyleSheet("")
        self.wavelength.setText("")
        self.wavelength.setObjectName("wavelength")
        self.horizontalLayout_3.addWidget(self.wavelength)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.cal_parameters)
        self.layoutWidget1.setGeometry(QtCore.QRect(290, 30, 239, 55))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chooseFolder = QtWidgets.QPushButton(self.layoutWidget1)
        self.chooseFolder.setCheckable(False)
        self.chooseFolder.setAutoExclusive(False)
        self.chooseFolder.setAutoDefault(False)
        self.chooseFolder.setDefault(True)
        self.chooseFolder.setFlat(True)
        self.chooseFolder.setObjectName("chooseFolder")
        self.horizontalLayout_4.addWidget(self.chooseFolder)
        self.labelDir = QtWidgets.QLineEdit(self.layoutWidget1)
        self.labelDir.setObjectName("labelDir")
        self.horizontalLayout_4.addWidget(self.labelDir)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelAvg = QtWidgets.QLabel(self.layoutWidget1)
        self.labelAvg.setEnabled(False)
        self.labelAvg.setStyleSheet("background : rgba(255,255,255,0)\n"
"")
        self.labelAvg.setLineWidth(0)
        self.labelAvg.setObjectName("labelAvg")
        self.horizontalLayout_5.addWidget(self.labelAvg)
        self.avg_time = QtWidgets.QLineEdit(self.layoutWidget1)
        self.avg_time.setMaximumSize(QtCore.QSize(280, 16777215))
        self.avg_time.setStyleSheet("")
        self.avg_time.setText("")
        self.avg_time.setObjectName("avg_time")
        self.horizontalLayout_5.addWidget(self.avg_time)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.layoutWidget2 = QtWidgets.QWidget(self.cal_parameters)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 120, 471, 252))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.startButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.startButton.setEnabled(True)
        self.startButton.setStyleSheet("")
        self.startButton.setCheckable(False)
        self.startButton.setAutoExclusive(False)
        self.startButton.setAutoDefault(False)
        self.startButton.setDefault(True)
        self.startButton.setFlat(True)
        self.startButton.setObjectName("startButton")
        self.verticalLayout_3.addWidget(self.startButton)
        self.textTemperature = QtWidgets.QTextBrowser(self.layoutWidget2)
        self.textTemperature.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textTemperature.setLineWrapColumnOrWidth(0)
        self.textTemperature.setObjectName("textTemperature")
        self.verticalLayout_3.addWidget(self.textTemperature)
        self.okButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.okButton.setEnabled(False)
        self.okButton.setStyleSheet("")
        self.okButton.setCheckable(False)
        self.okButton.setAutoExclusive(False)
        self.okButton.setAutoDefault(False)
        self.okButton.setDefault(True)
        self.okButton.setFlat(True)
        self.okButton.setObjectName("okButton")
        self.verticalLayout_3.addWidget(self.okButton)
        self.cal_values = QtWidgets.QGroupBox(self.Calibration)
        self.cal_values.setGeometry(QtCore.QRect(20, 440, 531, 431))
        self.cal_values.setStyleSheet("background : rgba(0,0,0,100);\n"
"color: rgb(255,255,255)")
        self.cal_values.setObjectName("cal_values")
        self.layoutWidget3 = QtWidgets.QWidget(self.cal_values)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 20, 361, 154))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelvalLum = QtWidgets.QLabel(self.layoutWidget3)
        self.labelvalLum.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelvalLum.setWordWrap(True)
        self.labelvalLum.setObjectName("labelvalLum")
        self.horizontalLayout_6.addWidget(self.labelvalLum)
        self.valLum = QtWidgets.QTextBrowser(self.layoutWidget3)
        self.valLum.setObjectName("valLum")
        self.horizontalLayout_6.addWidget(self.valLum)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelValPow = QtWidgets.QLabel(self.layoutWidget3)
        self.labelValPow.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelValPow.setObjectName("labelValPow")
        self.horizontalLayout_7.addWidget(self.labelValPow)
        self.valPow = QtWidgets.QTextBrowser(self.layoutWidget3)
        self.valPow.setObjectName("valPow")
        self.horizontalLayout_7.addWidget(self.valPow)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.Calibration, "")
        self.Sample = QtWidgets.QWidget()
        self.Sample.setObjectName("Sample")
        self.widgetDown = QtWidgets.QWidget(self.Sample)
        self.widgetDown.setEnabled(False)
        self.widgetDown.setGeometry(QtCore.QRect(760, 480, 591, 391))
        self.widgetDown.setAutoFillBackground(False)
        self.widgetDown.setStyleSheet("background-color: rgb(109,109,109);")
        self.widgetDown.setObjectName("widgetDown")
        self.widgetUp = QtWidgets.QWidget(self.Sample)
        self.widgetUp.setGeometry(QtCore.QRect(760, 30, 591, 431))
        self.widgetUp.setAutoFillBackground(False)
        self.widgetUp.setStyleSheet("background-color: rgb(109,109,109);")
        self.widgetUp.setObjectName("widgetUp")
        self.Val = QtWidgets.QGroupBox(self.Sample)
        self.Val.setGeometry(QtCore.QRect(10, 490, 741, 371))
        self.Val.setStyleSheet("background : rgba(0,0,0,100);\n"
"color: rgb(255,255,255)")
        self.Val.setObjectName("Val")
        self.labelvalResP = QtWidgets.QLabel(self.Val)
        self.labelvalResP.setGeometry(QtCore.QRect(55, 410, 101, 41))
        self.labelvalResP.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelvalResP.setScaledContents(False)
        self.labelvalResP.setWordWrap(True)
        self.labelvalResP.setObjectName("labelvalResP")
        self.valResidualsP = QtWidgets.QTextBrowser(self.Val)
        self.valResidualsP.setGeometry(QtCore.QRect(180, 410, 371, 50))
        self.valResidualsP.setObjectName("valResidualsP")
        self.layoutWidget1 = QtWidgets.QWidget(self.Val)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 341, 312))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.labelvalPowS = QtWidgets.QLabel(self.layoutWidget1)
        self.labelvalPowS.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelvalPowS.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelvalPowS.setObjectName("labelvalPowS")
        self.horizontalLayout_15.addWidget(self.labelvalPowS)
        self.valPowS = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.valPowS.setObjectName("valPowS")
        self.horizontalLayout_15.addWidget(self.valPowS)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.labelvalLum_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.labelvalLum_2.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelvalLum_2.setWordWrap(True)
        self.labelvalLum_2.setObjectName("labelvalLum_2")
        self.horizontalLayout_16.addWidget(self.labelvalLum_2)
        self.valLuminance = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.valLuminance.setObjectName("valLuminance")
        self.horizontalLayout_16.addWidget(self.valLuminance)
        self.verticalLayout_8.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.labelvalFitLum = QtWidgets.QLabel(self.layoutWidget1)
        self.labelvalFitLum.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelvalFitLum.setScaledContents(False)
        self.labelvalFitLum.setWordWrap(True)
        self.labelvalFitLum.setObjectName("labelvalFitLum")
        self.horizontalLayout_17.addWidget(self.labelvalFitLum)
        self.valFitLum = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.valFitLum.setObjectName("valFitLum")
        self.horizontalLayout_17.addWidget(self.valFitLum)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.labelvalRes = QtWidgets.QLabel(self.layoutWidget1)
        self.labelvalRes.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelvalRes.setScaledContents(False)
        self.labelvalRes.setWordWrap(True)
        self.labelvalRes.setObjectName("labelvalRes")
        self.horizontalLayout_18.addWidget(self.labelvalRes)
        self.valResiduals = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.valResiduals.setObjectName("valResiduals")
        self.horizontalLayout_18.addWidget(self.valResiduals)
        self.verticalLayout_8.addLayout(self.horizontalLayout_18)
        self.layoutWidget2 = QtWidgets.QWidget(self.Val)
        self.layoutWidget2.setGeometry(QtCore.QRect(370, 20, 321, 233))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.labelEm = QtWidgets.QLabel(self.layoutWidget2)
        self.labelEm.setEnabled(False)
        self.labelEm.setStyleSheet("background : rgba(255,255,255,0)\n"
"")
        self.labelEm.setLineWidth(0)
        self.labelEm.setObjectName("labelEm")
        self.horizontalLayout_19.addWidget(self.labelEm)
        self.valEps = QtWidgets.QTextBrowser(self.layoutWidget2)
        self.valEps.setObjectName("valEps")
        self.horizontalLayout_19.addWidget(self.valEps)
        self.verticalLayout_9.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.labelActTemp = QtWidgets.QLabel(self.layoutWidget2)
        self.labelActTemp.setEnabled(True)
        self.labelActTemp.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelActTemp.setObjectName("labelActTemp")
        self.horizontalLayout_20.addWidget(self.labelActTemp)
        self.valTemp = QtWidgets.QTextBrowser(self.layoutWidget2)
        self.valTemp.setObjectName("valTemp")
        self.horizontalLayout_20.addWidget(self.valTemp)
        self.verticalLayout_9.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.labelNbMeasure = QtWidgets.QLabel(self.layoutWidget2)
        self.labelNbMeasure.setEnabled(True)
        self.labelNbMeasure.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelNbMeasure.setObjectName("labelNbMeasure")
        self.horizontalLayout_21.addWidget(self.labelNbMeasure)
        self.valNbMeasure = QtWidgets.QTextBrowser(self.layoutWidget2)
        self.valNbMeasure.setObjectName("valNbMeasure")
        self.horizontalLayout_21.addWidget(self.valNbMeasure)
        self.verticalLayout_9.addLayout(self.horizontalLayout_21)
        self.Param = QtWidgets.QGroupBox(self.Sample)
        self.Param.setEnabled(True)
        self.Param.setGeometry(QtCore.QRect(20, 20, 731, 451))
        self.Param.setStyleSheet("background : rgba(0,0,0,100);\n"
"color: rgb(255,255,255)")
        self.Param.setObjectName("Param")
        self.check_simu = QtWidgets.QCheckBox(self.Param)
        self.check_simu.setGeometry(QtCore.QRect(20, 170, 76, 20))
        font = QtGui.QFont()
        font.setKerning(True)
        self.check_simu.setFont(font)
        self.check_simu.setObjectName("check_simu")
        self.layoutWidget3 = QtWidgets.QWidget(self.Param)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 40, 331, 121))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelVISAs = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelVISAs.setFont(font)
        self.labelVISAs.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelVISAs.setTextFormat(QtCore.Qt.PlainText)
        self.labelVISAs.setWordWrap(True)
        self.labelVISAs.setObjectName("labelVISAs")
        self.horizontalLayout_8.addWidget(self.labelVISAs)
        self.id_powermeterS = QtWidgets.QComboBox(self.layoutWidget3)
        self.id_powermeterS.setAutoFillBackground(False)
        self.id_powermeterS.setStyleSheet("")
        self.id_powermeterS.setEditable(False)
        self.id_powermeterS.setCurrentText("")
        self.id_powermeterS.setObjectName("id_powermeterS")
        self.horizontalLayout_8.addWidget(self.id_powermeterS)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelAvgs = QtWidgets.QLabel(self.layoutWidget3)
        self.labelAvgs.setEnabled(False)
        self.labelAvgs.setStyleSheet("background : rgba(255,255,255,0)\n"
"")
        self.labelAvgs.setLineWidth(0)
        self.labelAvgs.setWordWrap(True)
        self.labelAvgs.setObjectName("labelAvgs")
        self.horizontalLayout_9.addWidget(self.labelAvgs)
        self.avg_timeS = QtWidgets.QLineEdit(self.layoutWidget3)
        self.avg_timeS.setMaximumSize(QtCore.QSize(300, 16777215))
        self.avg_timeS.setStyleSheet("")
        self.avg_timeS.setText("")
        self.avg_timeS.setObjectName("avg_timeS")
        self.horizontalLayout_9.addWidget(self.avg_timeS)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.checkBoxSigma = QtWidgets.QCheckBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.checkBoxSigma.setFont(font)
        self.checkBoxSigma.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.checkBoxSigma.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBoxSigma.setChecked(False)
        self.checkBoxSigma.setObjectName("checkBoxSigma")
        self.verticalLayout_5.addWidget(self.checkBoxSigma)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelTempLim = QtWidgets.QLabel(self.layoutWidget3)
        self.labelTempLim.setEnabled(True)
        self.labelTempLim.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelTempLim.setScaledContents(False)
        self.labelTempLim.setWordWrap(True)
        self.labelTempLim.setObjectName("labelTempLim")
        self.horizontalLayout_10.addWidget(self.labelTempLim)
        self.temp_limit = QtWidgets.QLineEdit(self.layoutWidget3)
        self.temp_limit.setMaximumSize(QtCore.QSize(280, 16777215))
        self.temp_limit.setStyleSheet("")
        self.temp_limit.setText("")
        self.temp_limit.setObjectName("temp_limit")
        self.horizontalLayout_10.addWidget(self.temp_limit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.layoutWidget4 = QtWidgets.QWidget(self.Param)
        self.layoutWidget4.setGeometry(QtCore.QRect(360, 40, 362, 106))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.chooseFolderS = QtWidgets.QPushButton(self.layoutWidget4)
        self.chooseFolderS.setCheckable(False)
        self.chooseFolderS.setAutoExclusive(False)
        self.chooseFolderS.setAutoDefault(False)
        self.chooseFolderS.setDefault(True)
        self.chooseFolderS.setFlat(True)
        self.chooseFolderS.setObjectName("chooseFolderS")
        self.horizontalLayout_11.addWidget(self.chooseFolderS)
        self.labelDirS = QtWidgets.QLineEdit(self.layoutWidget4)
        self.labelDirS.setObjectName("labelDirS")
        self.horizontalLayout_11.addWidget(self.labelDirS)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.labelinit_guess = QtWidgets.QLabel(self.layoutWidget4)
        self.labelinit_guess.setEnabled(False)
        self.labelinit_guess.setStyleSheet("background : rgba(255,255,255,0)\n"
"")
        self.labelinit_guess.setLineWidth(0)
        self.labelinit_guess.setObjectName("labelinit_guess")
        self.horizontalLayout_12.addWidget(self.labelinit_guess)
        self.init_guess = QtWidgets.QLineEdit(self.layoutWidget4)
        self.init_guess.setMaximumSize(QtCore.QSize(300, 16777215))
        self.init_guess.setStyleSheet("")
        self.init_guess.setText("")
        self.init_guess.setObjectName("init_guess")
        self.horizontalLayout_12.addWidget(self.init_guess)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.checkBoxBounds = QtWidgets.QCheckBox(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.checkBoxBounds.setFont(font)
        self.checkBoxBounds.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.checkBoxBounds.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBoxBounds.setChecked(False)
        self.checkBoxBounds.setObjectName("checkBoxBounds")
        self.verticalLayout_6.addWidget(self.checkBoxBounds)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.labelEmlim = QtWidgets.QLabel(self.layoutWidget4)
        self.labelEmlim.setEnabled(True)
        self.labelEmlim.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelEmlim.setAutoFillBackground(False)
        self.labelEmlim.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelEmlim.setObjectName("labelEmlim")
        self.horizontalLayout_13.addWidget(self.labelEmlim)
        self.em_limit = QtWidgets.QLineEdit(self.layoutWidget4)
        self.em_limit.setMinimumSize(QtCore.QSize(280, 0))
        self.em_limit.setMaximumSize(QtCore.QSize(280, 16777215))
        self.em_limit.setStyleSheet("")
        self.em_limit.setText("")
        self.em_limit.setObjectName("em_limit")
        self.horizontalLayout_13.addWidget(self.em_limit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.layoutWidget5 = QtWidgets.QWidget(self.Param)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 390, 445, 43))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.startButtonS = QtWidgets.QPushButton(self.layoutWidget5)
        self.startButtonS.setEnabled(True)
        self.startButtonS.setStyleSheet("")
        self.startButtonS.setCheckable(False)
        self.startButtonS.setAutoExclusive(False)
        self.startButtonS.setDefault(True)
        self.startButtonS.setFlat(True)
        self.startButtonS.setObjectName("startButtonS")
        self.horizontalLayout_14.addWidget(self.startButtonS)
        self.stopButton = QtWidgets.QPushButton(self.layoutWidget5)
        self.stopButton.setEnabled(False)
        self.stopButton.setStyleSheet("")
        self.stopButton.setCheckable(False)
        self.stopButton.setAutoExclusive(False)
        self.stopButton.setAutoDefault(False)
        self.stopButton.setDefault(True)
        self.stopButton.setFlat(True)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_14.addWidget(self.stopButton)
        self.startContButtonS = QtWidgets.QPushButton(self.layoutWidget5)
        self.startContButtonS.setEnabled(True)
        self.startContButtonS.setStyleSheet("")
        self.startContButtonS.setCheckable(False)
        self.startContButtonS.setAutoExclusive(False)
        self.startContButtonS.setDefault(True)
        self.startContButtonS.setFlat(True)
        self.startContButtonS.setObjectName("startContButtonS")
        self.horizontalLayout_14.addWidget(self.startContButtonS)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelDelay = QtWidgets.QLabel(self.layoutWidget5)
        self.labelDelay.setEnabled(True)
        self.labelDelay.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelDelay.setAutoFillBackground(False)
        self.labelDelay.setStyleSheet("background : rgba(255,255,255,0)")
        self.labelDelay.setObjectName("labelDelay")
        self.verticalLayout_7.addWidget(self.labelDelay)
        self.delay = QtWidgets.QLineEdit(self.layoutWidget5)
        self.delay.setMinimumSize(QtCore.QSize(0, 0))
        self.delay.setMaximumSize(QtCore.QSize(280, 16777215))
        self.delay.setStyleSheet("")
        self.delay.setText("")
        self.delay.setObjectName("delay")
        self.verticalLayout_7.addWidget(self.delay)
        self.horizontalLayout_14.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.Sample, "")
        Pyro.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pyro)
        self.tabWidget.setCurrentIndex(0)
        self.checkBoxBounds.clicked['bool'].connect(self.temp_limit.setVisible) # type: ignore
        self.checkBoxBounds.clicked['bool'].connect(self.labelTempLim.setVisible) # type: ignore
        self.checkBoxBounds.clicked['bool'].connect(self.em_limit.setVisible) # type: ignore
        self.checkBoxBounds.clicked['bool'].connect(self.labelEmlim.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Pyro)

    def retranslateUi(self, Pyro):
        _translate = QtCore.QCoreApplication.translate
        Pyro.setWindowTitle(_translate("Pyro", "MainWindow"))
        self.cal_parameters.setTitle(_translate("Pyro", "Parameters"))
        self.labelVISA.setText(_translate("Pyro", "Power Meter VISA"))
        self.id_powermeter.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Instrument adress</span></p></body></html>"))
        self.labelTemp.setText(_translate("Pyro", "Temperatures [°C]"))
        self.temperature.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[T1,...,Ti,...,Tn] - Temperatures of calibration</span></p></body></html>"))
        self.labelWv.setText(_translate("Pyro", "Wavelengths [µm]"))
        self.wavelength.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[w1,...,wj,...,wn]</span></p></body></html>"))
        self.chooseFolder.setText(_translate("Pyro", "Choose folder"))
        self.labelAvg.setText(_translate("Pyro", "Averaging time [ms]"))
        self.avg_time.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[A1,...,Aj,...,Ap]</span></p></body></html>"))
        self.avg_time.setWhatsThis(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[A1,A2,A3,A4]</span></p></body></html>"))
        self.startButton.setText(_translate("Pyro", "Start"))
        self.textTemperature.setHtml(_translate("Pyro", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt; vertical-align:middle;\">Press Start when ready to measure</span></p></body></html>"))
        self.okButton.setText(_translate("Pyro", "OK"))
        self.cal_values.setTitle(_translate("Pyro", "Values"))
        self.labelvalLum.setText(_translate("Pyro", "Luminance [W.m-2.µm-1.str-1]"))
        self.valLum.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Luminance with Planck\'s law (emissivity = 1 ; T +/- correction of the blackbody, see blackbody_calibration.py)</span></p></body></html>"))
        self.labelValPow.setText(_translate("Pyro", "Power [W]"))
        self.valPow.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Power received by the photodiodes</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Calibration), _translate("Pyro", "Calibration"))
        self.Val.setTitle(_translate("Pyro", "Values"))
        self.labelvalResP.setText(_translate("Pyro", "Residuals [% luminance]"))
        self.valResidualsP.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Measured luminance - fitted luminance (using Planck\'s law with fitted T and E) in %</span></p></body></html>"))
        self.valResidualsP.setWhatsThis(_translate("Pyro", "Measured luminance - fitted luminance (using Planck\'s law with fitted T and E)"))
        self.labelvalPowS.setText(_translate("Pyro", "Power [W]"))
        self.valPowS.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Power received by the photodiodes</span></p></body></html>"))
        self.valPowS.setWhatsThis(_translate("Pyro", "Power received by the photodiodes"))
        self.labelvalLum_2.setText(_translate("Pyro", "Measured luminance [W.m-2.µm-1.str-1]"))
        self.valLuminance.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Measured luminance using the A,B &amp; C calibration coefficients </span></p></body></html>"))
        self.valLuminance.setWhatsThis(_translate("Pyro", "Measured luminance with the calibration coefficients"))
        self.labelvalFitLum.setText(_translate("Pyro", "Fitted luminance [W.m-2.µm-1.str-1]"))
        self.valFitLum.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Fitted luminance (using Planck\'s law with fitted T and E)</span></p></body></html>"))
        self.valFitLum.setWhatsThis(_translate("Pyro", "Measured luminance - fitted luminance (using Planck\'s law with fitted T and E)"))
        self.labelvalRes.setText(_translate("Pyro", "Residuals [luminance]"))
        self.valResiduals.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Measured luminance - fitted luminance (using Planck\'s law with fitted T and E)</span></p></body></html>"))
        self.valResiduals.setWhatsThis(_translate("Pyro", "Measured luminance - fitted luminance (using Planck\'s law with fitted T and E)"))
        self.labelEm.setText(_translate("Pyro", "Emissivity"))
        self.valEps.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Fitted emissivity</span></p></body></html>"))
        self.valEps.setWhatsThis(_translate("Pyro", "Fitted emissivity"))
        self.labelActTemp.setText(_translate("Pyro", "Actual temperature [°C]"))
        self.valTemp.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Fitted temperature</span></p></body></html>"))
        self.valTemp.setWhatsThis(_translate("Pyro", "Fitted temperature"))
        self.labelNbMeasure.setText(_translate("Pyro", "Times measured"))
        self.Param.setTitle(_translate("Pyro", "Parameters"))
        self.check_simu.setText(_translate("Pyro", "Simuler"))
        self.labelVISAs.setText(_translate("Pyro", "Power Meter VISA"))
        self.id_powermeterS.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Instrument adress</span></p></body></html>"))
        self.labelAvgs.setText(_translate("Pyro", "Averaging time [ms]"))
        self.avg_timeS.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[A1,...,Aj,...,Ap]</span></p></body></html>"))
        self.checkBoxSigma.setText(_translate("Pyro", "Add sigma = (1 / y²) when fitting"))
        self.labelTempLim.setText(_translate("Pyro", "Temperature limits [°C]"))
        self.temp_limit.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[Tmin, Tmax] bounds for the sample curve_fit function</span></p></body></html>"))
        self.temp_limit.setWhatsThis(_translate("Pyro", "[Tmin, Tmax] bounds for the sample curve_fit function"))
        self.chooseFolderS.setText(_translate("Pyro", "Choose folder"))
        self.labelDirS.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">Folder where the sample values, parameters and calibration values will be saved</span></p></body></html>"))
        self.labelinit_guess.setText(_translate("Pyro", "Initial Guesses"))
        self.init_guess.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[Tguess, Eguess] - Temperature (°C) and Emissivity at which the fit will start</span></p><p><span style=\" color:#aa55ff;\">If the fit cannot be made, try to lower the temperature </span></p></body></html>"))
        self.checkBoxBounds.setText(_translate("Pyro", "Add ε and T° bounds when fitting"))
        self.labelEmlim.setText(_translate("Pyro", "Emissivity limits"))
        self.em_limit.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[Emin, Emax] bounds for the sample curve_fit function</span></p></body></html>"))
        self.em_limit.setWhatsThis(_translate("Pyro", "[Emin, Emax] bounds for the sample curve_fit function"))
        self.startButtonS.setText(_translate("Pyro", "Start one measure"))
        self.stopButton.setText(_translate("Pyro", "Stop"))
        self.startContButtonS.setText(_translate("Pyro", "Start Continuous mode"))
        self.labelDelay.setText(_translate("Pyro", "Delay [s]"))
        self.delay.setToolTip(_translate("Pyro", "<html><head/><body><p><span style=\" color:#aa55ff;\">[Emin, Emax] bounds for the sample curve_fit function</span></p></body></html>"))
        self.delay.setWhatsThis(_translate("Pyro", "[Emin, Emax] bounds for the sample curve_fit function"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sample), _translate("Pyro", "Sample"))
