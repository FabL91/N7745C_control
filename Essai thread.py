    
"""_summary_"""

import sys
import time
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QHBoxLayout)
from PySide6.QtCore import QThread, QObject, Signal


class Worker(QObject):
    finished = Signal()
    valueChanged = Signal(int)

    def __init__(self):
        super().__init__()
        self.running = False
        self.value = 0

    def run(self):
        while self.running:
            self.value += 1
            self.valueChanged.emit(self.value)
            time.sleep(0.25)  # Pause for 0.25 seconds to simulate work
        self.finished.emit()  # Emit the finished signal when the work is done

    def start(self):
        self.running = True

    def stop(self):
        self.running = False


class MaPremiereFenetre(QWidget):
    def __init__(self):
        super().__init__()

        # Create a label
        self.label = QLabel("0", self)

        # Create buttons
        self.bouton_ok = QPushButton("Démarrer", self)
        self.bouton_stop = QPushButton("Arrêter", self)
        self.bouton_ok.clicked.connect(self.start_thread)
        self.bouton_stop.clicked.connect(self.stop_thread)

        # Create horizontal layout
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.bouton_ok)
        self.layout.addWidget(self.bouton_stop)

        # Set window geometry and layout
        self.setGeometry(300, 300, 250, 150)
        self.setLayout(self.layout)

        # Initialize thread and worker object
        self.thread = None
        self.worker = None

        # Start a new thread and worker
        self.create_thread_and_worker()

    def create_thread_and_worker(self):
        # Create new thread and worker object
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        # Connect signals and slots
        self.worker.valueChanged.connect(self.update_label)
        self.thread.started.connect(self.worker.run)  # Launch run when the thread starts
        self.worker.finished.connect(self.thread.quit)
        """self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)"""

    def stop_thread(self):
        if self.worker and self.worker.running:
            self.worker.stop()  # Stop the worker's loop

    def update_label(self, value):
        self.label.setText(str(value))

    def start_thread(self):
        if self.thread is None or not self.thread.isRunning():
            if self.thread is not None:  # If there's already a thread, clean it up
                self.thread.deleteLater()
            self.create_thread_and_worker()  # Recreate thread and worker

            self.worker.start()  # Set worker's running flag to True
            self.thread.start()  # Start the thread
        print("démarrer")
        print(self.thread)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = MaPremiereFenetre()
    fenetre.show()
    sys.exit(app.exec())

