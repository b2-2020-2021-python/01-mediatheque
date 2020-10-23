import os
from importlib import import_module

class DocumentFactory:

    def creerInstance(self, file):
        """ Méthode abstraite """
        pass



class DocumentFactoryPrincipale:
    """ Cette classe a pour rôle de trouver le bon type de Document dans le nom du fichier, et d'appeler la
    classe Factory correspondante.
    """

    __instance = None

    @staticmethod
    def getInstance():
        if __class__.__instance == None:  # Lazy loading
            __class__.__instance = __class__()
        return __class__.__instance


    def __init__(self):
        self._factories = {}

    def registerFactory(self, type, factory):
        self._factories[type] = factory

    def loadFactoryPlugins(self):
        """ Charge dynamiquement tous les modules présents dans le dossier actions"""
        main_dir = os.path.dirname(__file__)
        for file in os.listdir(main_dir + "/factories"):
            if file.endswith(".py"):
                import_module("factories." + file[:-3])

    def creerDocument(self, nomFichier):
        """ Créer une instance de Document à partir d'un fichier """
        main_dir = os.path.dirname(__file__)
        fichierSplit = nomFichier.split(".")  # split sur le point pour extraire l'extension
        print("Nom du fichier: " + fichierSplit[0])
        print("Type de document: " + fichierSplit[1])

        type = fichierSplit[1]
        with open(main_dir + "/documents/" + nomFichier, "r") as f:
            return self._factories[type].creerInstance(f)
