class EtatApp:

    # Code pour le Singleton
    __instance = None
    @staticmethod
    def getInstance():
        if EtatApp.__instance is None:
            EtatApp.__instance = EtatApp()
        return EtatApp.__instance

    # Code de la classe
    def __init__(self):
        self.etat = True

    def getEtat(self):
        return self.etat

    def terminerApp(self):
        self.etat = False


