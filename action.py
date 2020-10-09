import os
from importlib import import_module


class Action:

    def execute(self, param):
        """Abstraite"""

    def info(self):
        """donne les informations de l'action"""

    def help(self):
        """ donne une description longue de la commande """
        pass


class ActionManager:
    """ Rôle : gérer l'association mot clef/instance, récupérer la bonne instance en fonction de la commande demandée,
    et gérer les splits de l'entrée utilisateur pour récupérer commande et paramètres"""

    __instance = None

    @staticmethod
    def getInstance():
        if __class__.__instance == None:  # Lazy loading
            __class__.__instance = __class__()
        return __class__.__instance

    def __init__(self):
        self.actions = {}

    def registerCommand(self, cmd, instanceAction):
        self.actions[cmd] = instanceAction

    def loadActionPlugins(self):
        """ Charge dynamiquement tous les modules présents dans le dossier actions"""
        main_dir = os.path.dirname(__file__)
        for file in os.listdir(main_dir + "/actions"):
            if file.endswith(".py"):
                import_module("actions." + file[:-3])

    def executerEntreeUtilisateur(self, entreeUtilisateur):
        try:
            [action, param] = entreeUtilisateur.split(" ", 1)
        except ValueError:
            # Si ValueError, le split ne renvoie qu'un seul élément
            action = entreeUtilisateur
            param = ""
        self.executer(action, param)

        ## Autre façon de faire la même chose :
        # splitage = choix.split(" ", 1)
        # action = choix
        # param = ""
        # if len(splitage) > 1:
        #     action = splitage[0]
        #     param = splitage[1]

    def executer(self, cmd, param):
        try:
            self.actions[cmd].execute(param)
        except KeyError:
            print("Commande inconnue")

    def afficherCommandesDispo(self):
        for key, val in self.actions.items():
            print(key + ": " + val.info())
