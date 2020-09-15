from document import Document
from remplissageCatalogue import creerCatalogue

catalogue = creerCatalogue()

while True:

    print("Que voulez vous faire ?")
    print("  cat: Consulter le catalogue")
    print(" show: Consulter un document particulier")
    print(" quit: Quitter")
    choix = input("Votre choix ? #> ")

    if choix == "cat":
        # Afficher le catalogue
        index = 1
        for doc in catalogue:
            print(str(index) + ": " + doc.getTitre())
            index += 1

    elif choix == "show":
        # Afficher un document
        docNum = int(input("Quel numéro de document ? "))
        print(catalogue[docNum-1].consulter())

    elif choix == "quit":
        # Quitter
        break