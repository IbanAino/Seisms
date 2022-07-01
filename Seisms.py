"""
Iban FERNANDEZ, 2022, hivernage à Dumont d'Urville, TA72
Script pour télécharger les données sismiques journalières mondiales
Ce scritp contient un formulaire pour entrer le jour des données sismiques désirées.
Ensuite le script télécharge les données via internet et les affiche.
Ce script se base sur l'architecture logicielle Modèle-Vue-Controller (MVC)

Modules :
tkinter : affichage graphique
configparser : lire des fichiers de configuration
re : utiliser les expressions régulières
datetime : définir la date du jour
math : calculer l'arrondi de valeurs d'angles
"""

from Model import *
from View import *
from Controller import *

##
# class App
#
# Cette classe est la classe principale du programme d'où sont instanciés le Modèle, la Vue et le Controlleur.
#
#
##
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Seismes')

        # create a model
        model = Model()

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view and model
        view.set_Controller(controller)
        model.set_Controller(controller)

        controller.load_Station_Config()

if __name__ == '__main__':
    app = App()
    app.mainloop()