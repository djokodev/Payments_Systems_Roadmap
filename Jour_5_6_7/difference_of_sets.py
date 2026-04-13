"""
Write a code to returns a new set containing elements that are present in set1 but not in set2
"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


# Methode 1
new_set = set()

for i in set1:
    if i not in set2:
        new_set.add(i)

print(new_set)


# Methode 2
new_set_2 = set1.difference(set2)
print(new_set_2)

