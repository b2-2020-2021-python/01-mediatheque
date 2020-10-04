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