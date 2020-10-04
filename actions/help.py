from action import Action

class HelpAction(Action):

    def __init__(self,actions):
        self.actions = actions

    def execute(self, param):
        action = self.actions[param]
        print(action.help())

    def info(self):
        return "Affiche l'aide d'une commande"

    def help(self):
        return """Affiche l'aide d'une commande, passer la commande en paramètre"""
