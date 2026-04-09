`Jour 3 & 4: Fonctions avancées`

Ces deux jours étaient consacrés aux fonctions avancées en Python,
notamment le concept de fonctions comme objets c'est-à-dire qu'en
Python, une fonction peut être passée en argument à une autre fonction.

C'est un concept fondamental dans les systèmes de paiement : les règles
de frais changent souvent (campagnes, réglementation, type d'opération).
Séparer la logique de traitement de la logique de calcul des frais rend
le système flexible et maintenable.

J'ai également appris une leçon non technique importante : arrêter
d'avoir peur d'écrire du code qui ne fonctionne pas. Écrire, exécuter,
voir ce qui casse, comprendre, corriger. C'est comme ça qu'on progresse.

Exercice : une fonction apply_fee(transaction, fee_calculator) qui
applique des frais à une transaction via un calculateur passé en
paramètre. Deux calculateurs implémentés : flat_fee (100 FCFA fixe)
et percentage_fee (1.5% du montant).

