from documentFactory import DocumentFactory,DocumentFactoryPrincipale
from texte import Text

class TextFactory(DocumentFactory):

    def creerInstance(self, file):
        # Lecture de la première ligne (auteur)
        auteur = file.readline().split(":", 1)[1]
        # Lecture de la deuxième ligne (titre)
        titre = file.readline().split(":", 1)[1]
        # Lecture de tout le reste du fichier (contenu)
        contenu = file.read()
        return Text(titre, contenu, auteur)

DocumentFactoryPrincipale.getInstance().registerFactory("text", TextFactory())
