from action import Action
from catalogue import Catalogue

class CatalogueAction(Action):

    def __init__(self, catalogue):
        self.catalogue = catalogue

    def execute(self, param):
        index = 1
        for doc in self.catalogue.getDocument():
            print(str(index) + ": " + doc.getTitre())
            index += 1

    def info(self):
        return  "Consulter le catalogue"

    def help(self):
        return "Consulte le catalogue, ne prend aucun paramètre"
