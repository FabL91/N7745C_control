"""Example de thread et slots et signaux

Pour utiliser Matplotlib dans un thread avec PyQt, il est important de gérer correctement l’interface utilisateur et le rendu graphique, 
car Matplotlib n'est pas thread-safe. Voici une approche générale :
Création d'un thread : Utilisez le module QThread de PyQt pour créer un thread séparé.
Cela vous permettra d'exécuter des tâches de calcul intensif sans bloquer l'interface utilisateur.
Signal et Slot : Établissez une communication entre le thread et l'interface utilisateur en utilisant des signaux et des slots.
Lorsque le thread a terminé son traitement, il peut émettre un signal pour informer l'interface utilisateur de mettre à jour le graphique.
Mise à jour de Matplotlib : Dans le slot qui reçoit le signal,
utilisez les méthodes de Matplotlib pour mettre à jour le graphique. 
Assurez-vous que cette mise à jour se fait dans le thread principal de l'interface utilisateur.

Exemple de code : Voici un exemple simplifié :"""

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
import matplotlib.pyplot as plt

class Worker(QThread):

    data_ready = pyqtSignal(list)

    def run(self):
        # Effectuer des calculs ici

        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]# Exemple de données

        self.data_ready.emit(data)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.data_ready.connect(self.update_plot)
        self.worker.start()

    def update_plot(self, data):
        plt.plot(data)
        plt.show()

app = QApplication([])
window = MainWindow()
#window.show()
app.exec_()