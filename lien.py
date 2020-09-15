from document import Document


class Lien(Document):
    """
    Classe abstraite : Un Document qui contient un lien
    """

    def __init__(self, titre, lien):
        Document.__init__(self, titre)
        self._lien = lien

    def getLien(self):
        return self._lien

    def consulter(self):
        """ Redéfinition de la méthode abstraite de la classe mère """
        return self.getTitre() + ": " + self._lien
    