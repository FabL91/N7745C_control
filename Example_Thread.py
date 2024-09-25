"""Pourquoi utiliser les QThreads ?

Dans les applications graphiques avec PyQt, les QThreads sont essentiels pour éviter que ton interface utilisateur (UI) ne se bloque
pendant l'exécution de tâches longues.
Imagine que tu veux télécharger une image ou effectuer un calcul complexe : si tu fais ça directement dans le thread principal (celui qui gère l'affichage), 
ton programme va sembler "planté" pendant tout ce temps.
Les QThreads permettent de déplacer ces tâches en arrière-plan, libérant ainsi ton UI pour qu'elle reste réactive.

Comment ça marche ?

    Créer un objet QThread: C'est comme créer un nouveau fil d'exécution.
    Définir une classe de travailleur: Cette classe va contenir la tâche que tu veux exécuter en arrière-plan.
    Elle devra émettre des signaux pour communiquer avec ton UI (par exemple, pour indiquer la progression d'une tâche).
    Déplacer le travailleur vers le thread: On utilise la méthode moveToThread pour associer la classe de travailleur à un thread spécifique.
    Connecter les signaux et les slots: Les signaux émis par le travailleur seront connectés à des slots de ton UI pour mettre à jour l'affichage.
    Démarrer le thread: Un simple appel à la méthode start() suffira pour lancer le thread."""
import time
import sys
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QVBoxLayout

class Workerfast(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run_1(self):
        # Simuler une tâche longue
        for i in range(100):
            # Remplace cette ligne par ta vraie tâche
            # Par exemple, un traitement de données, un téléchargement.
            print(f"Progression : {i+1}%")
            self.progress.emit(i+1)
            time.sleep(0.05)
            
        self.finished.emit()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # ... (initialisation de la fenêtre)
        self.progressBar = QProgressBar()
        
         # Créer une barre de progression
        
        self.progressBar.setRange(0, 100)

        # Créer un layout et ajouter la barre de progression
        layout = QVBoxLayout()
        layout.addWidget(self.progressBar)
        self.setLayout(layout)


        # Créer un worker et un thread
        self.worker = Workerfast()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)

        # Connecter les signaux
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.progressBar.setValue)

        # Démarrer le worker
        self.thread.started.connect(self.worker.run_1)
        self.thread.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())