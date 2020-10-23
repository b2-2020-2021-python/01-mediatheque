## Ajout du pattern Command

### 1/ Créer l'interface Action (fichier action.py)
L'interface ne contient qu'une méthode *execute()*

### 2/ Créer les classes filles qui implémentent l'interface Action.

3 Actions :

- cat : afficher le catalogue
- show : afficher un document
- quit : quitter le programme

On va mettre toutes les implémentations dans un dossier *action* pour ranger nos classes.

=> Pour importer les classes d'un sous dossier, il faut mettre un "." à chaque dossier :

```
from actions.catalogue import CalatogueAction
```

### 3/ Ajout de l'action quit

Problème : la boucle while du main se terminait via un break exécuté par l'action "quit".
Si on déplace le code de l'action dans une classe séparée, on n'a plus la possibilité de faire ce `break`.

Solution : l'état de l'app (en cours ou non) doit être partagé entre le main et l'action Quit, on va donc le sortir du
main et le mettre dans un Singleton pour qu'on puisse y accéder partout dans le code.

## Chargement dynamique des commandes

Toutes les classes filles d'action sont créées dans un sous dossier *actions*.
Le code qui fait appel à la méthode **ActionManager.register()** actuellement dans le main avec les noms des actions hardocé doit être déplacé dans le module de chaque Action.
Ainsi, chaque Action a la responsabilité de s'enregistrer elle même.

### Transformer l'ActionManager en Singleton
Pour qu'un module Action puisse accéder à l'ActionManager, ce dernier ne peut plus être instancié dans le main. On va en faire un Singleton.
Pour transformer n'importe quelle classe en Singleton en Python, il suffit de lui ajouter ce code :

```python
__instance = None

@staticmethod
def getInstance():
    if __class__.__instance == None:  # Lazy loading
        __class__.__instance = __class__()
    return __class__.__instance
```

### Gérer l'enregistrement des Actions dans les modules d'action

On déplace le code de l'appel à `ActionManager.register()` du main vers le code du module lui même.
Les dépendences passées au constructeur (intialement créées dans le main) ne sont plus accessible, il faut en faire également
des Singleton. C'est le cas uniquement pour le *catalogue*.

Exemple pour la commande d'affichage du catalogue :

```python
ActionManager.getInstance().registerCommand("cat",CatalogueAction(Catalogue.getInstance() ))
``` 

### Chargement dynamique des modules d'action

Il ne reste plus qu'à charger dynamiquement tous les modules présents dans le dossier *actions*. Les modules
vont enregistrer eux même l'Action auprès de l'ActionManager et seront ainsi disponibles dans le main.

```python
main_dir = os.path.dirname(__file__)
for file in os.listdir(main_dir + "/actions"):
    if file.endswith(".py"):
        import_module("actions." + file[:-3])
```


## Mise en place des Factory

### Lecture de fichier

Les documents seront enregistrés dans des fichiers textes chargés au démarrage plutôt qu'harcodés dans la classe *Catalogue*.
Tous les documents auront pour extension ".type.txt*, où *type* est la clef du type de document (text, image).

Au démarrage du programme, on va lire tous les fichiers *\*.txt* présents dans le dossier *documents*, et le passer
à la factory qui gère le type indiqué dans l'extension du fichier. Chaque sous classe de Factory (une par type) a en charge
de lire et d'interpréter le contenu du fichier pour créer l'instance du type adéquat.

Exemple de code pour lire tous les fichiers présents dans le dossier *documents* :

```python
import os

main_dir = os.path.dirname(__file__)
for file in os.listdir(main_dir + "/documents"):
    if file.endswith(".txt"): # On ne traite que les fichiers txt
        fichierSplit = file.split(".") # split sur le point pour extraire l'extension
        print("Nom du fichier: "+fichierSplit[0])
        print("Type de document: "+fichierSplit[1])

        # Ouverture du fichier
        with open(main_dir + "/documents/" + file, "r") as f:
            # Lecture de la première ligne (auteur)
            auteur = f.readline()
            # Lecture de la deuxième ligne (titre)
            titre = f.readline()
            # Lecture de la troisième ligne (lien)
            lien = f.readline()
            # Lecture de tout le reste du fichier (contenu)
            contenu = f.read()
```

Ce qu'il faut retenir pour la lecture de fichiers textes ([lien vers la doc](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)) :

- ouvrir un fichier en lecture : `f = open(filename, "r")`

- utiliser plutôt un bloc `with` pour gérer automatiquement la fermeture du fichier (cf doc)

- lire une ligne : `f.readline()`. Attention, la ligne contient également le retour à la ligne final

- lire tout le fichier : `f.read()`

- boucler ligne par ligne : `for line in f:`

Lors des opérations de lecture, le descripteur de fichier maintien un cursor sur la position actuelle :
plusieurs appels à `readline()` avancent dans la lecture du fichier, et l'appel à `read()` renvoie tout le reste
à partir de la position de lecture.

### Mise en place du pattern Factory

Le code de création des Documents est supprimé du constructeur du catalogue. Les documents sont chargés directement à partir des fichiers présents dans le dossier *documents*.

A chaque type de document correspond une factory (définie dans le dossier *factories*) qui a pour rôle de créer une instance d'un sous-type document à partir d'un fichier.

C'est en fonction de l'extension du fichier (*.image.txt, *.text.txt) que l'on identifie la factory à utiliser. Cette selection est opéré dans la classe `DocumentFactoryPrincipale`
qui maintient un dictionnaire qui fait le lien entre le nom du type présent dans l'extension du fichier et la classe Factory correspondante.

Cette classe a deux rôles :

- elle est le point d'entrée du pattern : on appelle `DocumentFactoryPrincipale.creerDocument(nomDuFichier)` pour faire créer l'instance de Document correspondant au fichier.
- elle permet à chaque sous-factory de s'enregistrer sur un type d'extention avec la méthode `DocumentFactoryPrincipale.registerFactory(type, factory)`

Comme pour le pattern Action, chaque type de Factory s'enregistre elle même lors du chargement du module. La méthode `DocumentFactoryPrincipale.loadFactoryPlugins()` s'occupe
de charger tous les modules présents dans le dossier *factories*.