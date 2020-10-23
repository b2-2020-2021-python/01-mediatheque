from texte import Text
from image import Image

class Catalogue:
        instance = None

        @staticmethod
        def getInstance():
            if Catalogue.instance is None:
                Catalogue.instance = Catalogue()
            return Catalogue.instance

        def ajouterDocument(self,doc):
            self._documents.append(doc)

        def __init__(self):
            self._documents = []

        def getDocument(self):
            return self._documents


