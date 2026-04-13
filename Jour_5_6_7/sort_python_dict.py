# -----------------------------
# O1: Trier un dictionnaire par ses valeurs (ordre croissant)
# -----------------------------

d = {'watermelon': 3, 'apple': 2, 'banana': 1}        

# liste de couple de valeur de type dict_items
print(d.items())

# Trie le dictionnaire par ses valeurs :
# - d.items() fournit des paires (clé, valeur)
# - sorted(..., key=lambda item: item[1]) trie ces paires selon la valeur
# - la dict comprehension reconstruit un dictionnaire à partir des éléments triés
asc = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

print(asc)



# -----------------------------
# O2: other implementation, 
# -----------------------------
from collections import OrderedDict

d = {'monday': 10, 'tuesday': 9, 'wednesday': 15}

res = OrderedDict(sorted(d.items(), key=lambda item: item[1]))

print(res)