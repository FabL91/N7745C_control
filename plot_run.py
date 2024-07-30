import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

from interface import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        
        super().__init__()
        # add the features of Ui_MainWindow() with the setupUi method accessible via sel.ui
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)  # Configurer l'interface
        
        self.frame = self.ui.frame  # Utilisation directe de l'élément de l'interface chargée
        # Initialiser Matplotlib
        self.init_matplotlib()
        
    def init_matplotlib(self):
        # Créer une figure Matplotlib
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, self)

        # Ajouter le canevas au QFrame
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)
        self.frame.setLayout(layout)
        
        

        # Tracer quelque chose
        self.plot()

    def plot(self):
        # Exemple de tracé
        ax = self.figure.add_subplot(111)
        ax.plot([0, 1, 2, 3], [10, 1, 20, 3])
        self.canvas.draw()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
