from documentFactory import DocumentFactory, DocumentFactoryPrincipale
from image import Image

class ImageFactory(DocumentFactory):

    def creerInstance(self, file):
        # Lecture de la première ligne (auteur)
        auteur = file.readline().split(":", 1)[1]
        # Lecture de la deuxième ligne (titre)
        titre = file.readline().split(":", 1)[1]
        # Lecture de la troisième ligne (lien)
        lien = file.readline().split(":", 1)[1]
        # Lecture de tout le reste du fichier (contenu)
        contenu = file.read()
        return Image(titre, contenu, auteur, lien)


DocumentFactoryPrincipale.getInstance().registerFactory("image", ImageFactory())
