from catalogue import Catalogue
from actions.catalogue import CatalogueAction
from actions.afficher import AfficherAction
from actions.quitter import QuitterAction
from actions.help import HelpAction
from etatApp import EtatApp
from action import ActionManager

catalogue = Catalogue.getInstance()

# La liste des actions avec leur mot clef
actionManager = ActionManager()
actionManager.registerCommand("cat",CatalogueAction(catalogue))
actionManager.registerCommand("show",AfficherAction(catalogue))
actionManager.registerCommand(("quit",QuitterAction()))
actionManager.registerCommand("help",HelpAction(actionManager))



while EtatApp.getInstance().getEtat():

    # Afficher commandes dispo
    print("Que voulez vous faire ?")
    actionManager.afficherCommandesDispo()

    # Récupérer entrée utilisateur
    choix = input("Votre choix ? #> ")

   # Exécuter la commande
    actionManager.executerEntreeUtilisateur(choix)

