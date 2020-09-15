class Document:
    """
    Classe abstraite : Un Document
    Il a un titre et peut être consulté
    """

    def __init__(self, titre):
        self._titre = titre

    def getTitre(self):
        return self._titre

    def consulter(self):
        """ Méthode abtraite """
        raise PermissionError()

    