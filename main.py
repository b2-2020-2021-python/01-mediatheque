from catalogue import Catalogue
from etatApp import EtatApp
from action import ActionManager
import os
from documentFactory import DocumentFactoryPrincipale


catalogue = Catalogue.getInstance()
factory = DocumentFactoryPrincipale.getInstance()
factory.loadFactoryPlugins()

# Création des documents du catalogue
main_dir = os.path.dirname(__file__)
for file in os.listdir(main_dir + "/documents"):
    if file.endswith(".txt"): # On ne traite que les fichiers txt
        doc = factory.creerDocument(file)
        catalogue.ajouterDocument(doc)

print(catalogue.getDocument())

# Gestion des actions
actionManager = ActionManager.getInstance()
actionManager.loadActionPlugins()

while EtatApp.getInstance().getEtat():

    # Afficher commandes dispo
    print("Que voulez vous faire ?")
    actionManager.afficherCommandesDispo()

    # Récupérer entrée utilisateur
    choix = input("Votre choix ? #> ")

   # Exécuter la commande
    actionManager.executerEntreeUtilisateur(choix)

