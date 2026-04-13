`Jours 5-6-7 : Décorateurs et pratique des structures de données`

Ces jours ont été divisés en deux axes.

Premier axe : pratique sur les structures de données vues
précédemment (dictionnaires, sets, comprehensions) via les exercices
de PYnative. L'objectif était de solidifier les réflexes avant de
passer à la suite. Les fichiers présents dans ce dossier en sont
le résultat direct.

Deuxième axe: les décorateurs Python.

Trois décorateurs implémentés dans le contexte des systèmes de paiement :

- @log_execution : affiche le nom de la fonction, ses arguments,
  et son temps d'exécution
- @retry(max_attempts) : réessaie automatiquement une fonction
  qui échoue, jusqu'à un nombre maximum de tentatives
- @validate_amount : vérifie que le montant est strictement positif
  et inférieur à 2 000 000 FCFA avant d'exécuter la fonction

Ressource principale : Real Python "Primer on Python Decorators"