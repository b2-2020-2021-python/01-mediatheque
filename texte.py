from document import Document

class Text(Document):
    """
    Un document de type Texte qui contient le contenu complet en mode texte du document (livre par exemple)
    """

    def __init__(self, titre, contenu, auteur):
        Document.__init__(self, titre)
        self._contenu = contenu
        self._auteur = auteur

    def consulter(self):
        """ Redéfinition de la méthode abstraite de la classe Document
        Affiche tout le texte du Document
        """
        returnValue = ""
        returnValue += "Titre : " + self.getTitre() + "\n"
        returnValue += "par " + self._auteur + "\n"
        returnValue += "    -~-~-~-~-~-~-~-~-" + "\n"
        returnValue += self._contenu + "\n"
        return returnValue
