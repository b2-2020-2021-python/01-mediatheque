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

    def __init__(self):
        self.actions = {}

    def registerCommand(self, cmd, instanceAction):
        self.actions[cmd] = instanceAction

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
