from lien import Lien

class Image(Lien):
    """ Représente une image
    """

    def __init__(self, titre, asciiart, auteur, lien):
        Lien.__init__(self, titre, lien)
        self._asciiart = asciiart
        self._auteur = auteur

    def consulter(self):
        """ Redéfinition de la méthode abstraite de la classe Document
        Affiche tout le texte du Document
        """
        returnValue = ""
        returnValue += "Oeuvre : " + self.getTitre() + "\n"
        returnValue += "Auteur " + self._auteur + "\n"
        returnValue += "\n"
        returnValue += self._asciiart + "\n" + "\n"
        returnValue += super().consulter()

        return returnValue


