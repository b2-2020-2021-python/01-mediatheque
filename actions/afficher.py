from action import Action
from catalogue import Catalogue

class AfficherAction(Action):

    def __init__(self, catalogue):
        self.catalogue = catalogue

    def execute(self, param):
        # Afficher un document
        docNum = int(param)
        print(self.catalogue.getDocument()[docNum - 1].consulter())

    def info(self):
        return "Consulter un document particulier"

    def help(self):
        return """Affiche un document du catalogue
Paramètres : un entier qui correspond au numéro du document à afficher
Attention, ne pas taper autre chose qu'un entier sinon ça plante !
"""



