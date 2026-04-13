"""
Write a code to return a new set containing only the elements that are common to both set1 and set2
"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


# Methode 1
set_intersection_1= set()

for i in set1:
    for j in set2:
        if i == j:
            set_intersection_1.add(i)

print(set_intersection_1)


# methode 2
set_intersection_2 = set1.intersection(set2)
print(set_intersection_2)


