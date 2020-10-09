from action import Action, ActionManager
from etatApp import EtatApp

class QuitterAction(Action):
    def execute(self, param):
        EtatApp.getInstance().terminerApp()

    def info(self):
        return "Quitter"

    def help(self):
        return """Quitte l'application, ne prend aucun paramètre"""


ActionManager.getInstance().registerCommand("quit",QuitterAction())
