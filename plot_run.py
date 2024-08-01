import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np

from interface import Ui_MainWindow
#plt.style.use('_mpl-gallery-nogrid')

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
        #self.figure = Figure()
        self.figure_g1 = plt.figure(layout='tight')
        self.canvas_g1 = FigureCanvas(self.figure_g1)
        

        toolbar_g1 = NavigationToolbar(self.canvas_g1, self)
        
        # Ajouter le canevas au QFrame
        graph_1 = QVBoxLayout()
        graph_1.addWidget(toolbar_g1)
        graph_1.addWidget(self.canvas_g1)
        self.frame.setLayout(graph_1)

               

        # Tracer quelque chose
        self.plot_graph1()
        

    def plot_graph1(self):
        # Exemple de tracé
        
        #ax.plot([0, 1, 2, 3], [10, 1, 20, 3])

        # make data
        x = np.linspace(0, 10, 100)
        y = 4 + 1 * np.sin(2 * x)
        x2 = np.linspace(0, 10, 25)
        y2 = 4 + 1 * np.sin(3 * x2)
        y3 = 4 + 1 * np.cos(2 * x)
        y4 = 4 + 1 * np.cos(3 * x2)

        # Créer un axe à partir de la figure existante
        ax1 = self.figure_g1.add_subplot(2, 1, 1)
        ax2 = self.figure_g1.add_subplot(2, 1, 2)

        ax1.plot(x2, y2 + 2.5, 'x', markeredgewidth=2, label='sinusoïd croix')
        ax1.plot(x, y, color='tab:orange', linewidth=2.0, label='sinusoïd line')
        ax1.plot(x2, y2 - 2.5, 'o-', linewidth=2)

        ax1.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 8), yticks=np.arange(1, 8))
        ax1.set_xlabel("Timing")
        ax1.set_ylabel("Amplitude")
        ax1.grid()
        ax1.legend()

        # Tracé pour le deuxième subplot
        ax2.plot(x2, y4 + 2.5, 'x', markeredgewidth=2, label='cosinus croix')
        ax2.plot(x, y3, color='tab:blue', linewidth=2.0, label='cosinus line')
        ax2.plot(x2, y4 - 2.5, 'o-', linewidth=2)

        ax2.set(xlim=(0, 8), xticks=np.arange(1, 8),
                ylim=(0, 8), yticks=np.arange(1, 8))
        ax2.set_xlabel("Timing")
        ax2.set_ylabel("Amplitude")
        ax2.grid()
        ax2.legend()

        self.canvas_g1.draw()

    """Conversion .ui to .py Pyqt5"""
    #pyuic5 interface.ui -o interface.py


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
