from catalogue import Catalogue
from etatApp import EtatApp
from action import ActionManager
import os

catalogue = Catalogue.getInstance()

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

