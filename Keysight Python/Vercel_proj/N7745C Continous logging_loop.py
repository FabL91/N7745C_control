import sys
import time
import numpy as np
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QProgressBar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.widgets import Cursor
import pyvisa
from collections import deque

class LoggingThread(QThread):
    data_ready = pyqtSignal(list)
    progress_update = pyqtSignal(int)

    def __init__(self, n7745c, points, integration_time, time_unit, loop_delay, parent=None):
        super().__init__(parent)
        self.n7745c = n7745c
        self.running = False
        self.points = points
        self.integration_time = integration_time
        self.time_unit = time_unit
        self.loop_delay = loop_delay
        self.calculate_sleep_time()

    def calculate_sleep_time(self):
        if self.time_unit == "US":
            self.sleep_time = (self.points * self.integration_time) / 1_000_000  # Convert to seconds
            self.time_int = self.integration_time/1_000_000
        elif self.time_unit == "MS":
            self.sleep_time = (self.points * self.integration_time) / 1000  # Convert to seconds
            self.time_int = self.integration_time/1000
        else:  # "S"
            self.sleep_time = self.points * self.integration_time
            self.time_int = self.integration_time

    def run(self):
        self.running = True
        self.n7745c.write(":SENSe2:FUNCtion:STATe LOGG,STAR")  # Enables the logging
        
        while self.running:
            data_1 = 0
            time.sleep(self.loop_delay)
            
            while data_1 == 0 and self.running:
                print(f"La valeur de data est toujours {data_1}")
                                
                data_1 = self.n7745c.query(":SENS2:FUNC:RES:IND?")
                
                        
            if self.running:
                #time.sleep(0.2)
                progress = 0
                for i in range(self.points):
                    progress = (100/self.points)*(i+1)
                    
                    self.progress_update.emit(progress)
                    time.sleep(self.time_int)
                    print (self.time_int)

                data = self.n7745c.query_binary_values(':SENSE2:CHANnel:FUNCtion:RESult?', 'f', False)
                print(data)
                print(len(data))
                print(data_1)
                self.data_ready.emit(data)
                                
        
        self.n7745c.write(":SENSe2:FUNCtion:STATe LOGG,STOP")  # Disables the logging

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        # Initialize VISA resource
        rm = pyvisa.ResourceManager()

        self.n7745c = rm.open_resource('TCPIP0::169.254.241.203::inst0::INSTR')

        self.n7745c.write(":SENSe2:FUNCtion:STATe LOGG,STOP") #Enables/Disables the logging, MinMax, or stability data acquisition function mode
        self.n7745c.write(":SENSe2:POWer:GAIN:AUTO 0") #Set the Auto Gain
        self.n7745c.write(":SENSe2:POWer:RANGe:AUTO 0") #Enables or disables automatic power ranging for the slot
        self.n7745c.write(":SENSe2:POWer:RANGe:UPPer -10 DBM") #Sets the power range for the module.
        self.n7745c.write(":SENSe2:POWer:UNIT 1") #Sets the sensor power unit 
        self.n7745c.write(":SENSe2:POWer:WAVelength 1552NM")#Sets the sensor wavelength.
        self.n7745c.write(":TRIGger2:INPut IGN")#Sets the incoming trigger response and arms the slot


        self.n7745c.write(":SENSe2:FUNCtion:LOOP 0")



        # Initialize data storage for the scrolling plot
        self.time_data = deque(maxlen=100)  # Store the last 100 time points
        self.first_point_data = deque(maxlen=100)  # Store the last 100 values of the first point
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_second_graph)
        self.update_timer.start(50)  # 500 ms = 0.5 seconds
        self.pending_data = None
        self.current_data = []

    def initUI(self):
        self.setWindowTitle("N7745C Continuous Logging")
        self.setGeometry(100, 100, 800, 800)  # Increased height to accommodate the second graph

        layout = QtWidgets.QVBoxLayout()

        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        self.startButton = QtWidgets.QPushButton("Start")
        self.stopButton = QtWidgets.QPushButton("Stop")
        self.startButton.clicked.connect(self.start_logging)
        self.stopButton.clicked.connect(self.stop_logging)
        button_layout.addWidget(self.startButton)
        button_layout.addWidget(self.stopButton)
        layout.addLayout(button_layout)

        # Input fields
        input_layout = QtWidgets.QHBoxLayout()
        self.pointsLineEdit = QtWidgets.QLineEdit("10")
        self.integrationTimeLineEdit = QtWidgets.QLineEdit("10")
        self.timeUnitComboBox = QtWidgets.QComboBox()
        self.timeUnitComboBox.addItems(["US", "MS", "S"])
        self.timeUnitComboBox.setCurrentText("MS")
        input_layout.addWidget(QtWidgets.QLabel("Number of Points:"))
        input_layout.addWidget(self.pointsLineEdit)
        input_layout.addWidget(QtWidgets.QLabel("Integration Time:"))
        input_layout.addWidget(self.integrationTimeLineEdit)
        input_layout.addWidget(self.timeUnitComboBox)
        self.delayLineEdit = QtWidgets.QLineEdit("0.1")
        input_layout.addWidget(QtWidgets.QLabel("Loop Delay (s):"))
        input_layout.addWidget(self.delayLineEdit)
        layout.addLayout(input_layout)

        # Cursor position display
        cursor_layout = QtWidgets.QHBoxLayout()
        self.cursor_x_edit = QtWidgets.QLineEdit()
        self.cursor_y_edit = QtWidgets.QLineEdit()
        self.cursor_x_edit.setReadOnly(True)
        self.cursor_y_edit.setReadOnly(True)
        cursor_layout.addWidget(QtWidgets.QLabel("Cursor X:"))
        cursor_layout.addWidget(self.cursor_x_edit)
        cursor_layout.addWidget(QtWidgets.QLabel("Cursor Y:"))
        cursor_layout.addWidget(self.cursor_y_edit)
        layout.addLayout(cursor_layout)

        # Progress bar
        self.progressBar = QProgressBar(self)
        layout.addWidget(self.progressBar)

        # Matplotlib figures
        self.figure1, self.ax1 = plt.subplots()
        self.canvas1 = FigureCanvas(self.figure1)
        layout.addWidget(self.canvas1)

        self.figure2, self.ax2 = plt.subplots()
        self.canvas2 = FigureCanvas(self.figure2)
        layout.addWidget(self.canvas2)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Set up the cursor
        self.cursor = Cursor(self.ax1, useblit=True, color='red', linewidth=1)
        self.canvas1.mpl_connect('motion_notify_event', self.on_mouse_move)

    def on_mouse_move(self, event):
        if event.inaxes:
            x, y = event.xdata, event.ydata
            self.cursor_x_edit.setText(f"{x:.2f}")
            self.cursor_y_edit.setText(f"{y:.2f}")

    def start_logging(self):
        points = int(self.pointsLineEdit.text())
        integration_time = int(self.integrationTimeLineEdit.text())
        time_unit = self.timeUnitComboBox.currentText()
        loop_delay = float(self.delayLineEdit.text())
        
        self.n7745c.write(f":SENSe2:FUNCtion:PARameter:LOGGing {points},{integration_time} {time_unit}")
        
        self.logging_thread = LoggingThread(self.n7745c, points, integration_time, time_unit, loop_delay)
        self.logging_thread.data_ready.connect(self.update_plot)
        self.progressBar.setValue(0)
        self.logging_thread.progress_update.connect(self.update_progress_bar)
        self.logging_thread.start()
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)

        # Reset the data storage for the scrolling plot
        self.time_data.clear()
        self.first_point_data.clear()
        self.update_timer.start(1)

    def stop_logging(self):
        self.logging_thread.running = False
        self.logging_thread.wait()
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.update_timer.stop()

    def update_plot(self, data):
        self.current_data = data
        # Update the first plot (all data points)
        self.ax1.clear()
        self.ax1.plot(data)
        self.ax1.set_title('N7745C Logging Data')
        self.ax1.set_xlabel('Sample')
        self.ax1.set_ylabel('Value')
        self.canvas1.draw()

        # Store the new data point for the second graph
        self.pending_data = data[0]

    def update_second_graph(self):
        if self.pending_data is not None:
            if len(self.time_data) == 0:
                self.time_data.append(0)
            else:
                self.time_data.append(self.time_data[-1] + 1)
            self.first_point_data.append(self.pending_data)

            self.ax2.clear()
            self.ax2.plot(list(self.time_data), list(self.first_point_data))
            self.ax2.set_title('First Data Point Over Time')
            self.ax2.set_xlabel('Time')
            self.ax2.set_ylabel('Value')
            self.ax2.set_xlim(max(0, self.time_data[-1] - 100), self.time_data[-1])
            self.canvas2.draw()

            self.pending_data = None

    def update_progress_bar(self, value):
        self.progressBar.setValue(value)

    def closeEvent(self, event):
        self.stop_logging()
        self.n7745c.close()
        event.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

