
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

"""
Perform following operations on given dictionary

1. Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
2. Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
3. Check if Key Exists in the dictionary
"""

del my_dict['profession']
print(my_dict)

for key, value in my_dict.items():
    print(key, value)
    
    
for key, value in my_dict.items():
    if key == 'age':
        print(True)