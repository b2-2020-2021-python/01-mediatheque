from document import Document
from catalogue import Catalogue

catalogue = Catalogue.getInstance()

while True:

    print("Que voulez vous faire ?")
    print("  cat: Consulter le catalogue")
    print(" show: Consulter un document particulier")
    print(" quit: Quitter")
    choix = input("Votre choix ? #> ")

    if choix == "cat":
        # Afficher le catalogue
        index = 1
        for doc in catalogue.getDocument():
            print(str(index) + ": " + doc.getTitre())
            index += 1

    elif choix == "show":
        # Afficher un document
        docNum = int(input("Quel numéro de document ? "))
        print(catalogue.getDocument()[docNum-1].consulter())

    elif choix == "quit":
        # Quitter
        break