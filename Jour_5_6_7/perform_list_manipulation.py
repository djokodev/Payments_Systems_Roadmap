"""
Perform following list manipulation operations on given list

Change Element: Change the second element of a list to 200 and print the updated list.
Append Element: Add 600 on the end of a list and print the new list.
Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
Remove Element (by value): Remove 600 from the list and print the list.
Remove Element (by index): Remove the element at index 0 from the list print the list.
"""

my_list = [10, 20, 30, 40, 50]

my_list[1] = 200
print(my_list)


my_list.append(600)
print(my_list)


my_list.insert(2, 300)
print(my_list)

my_list.pop()
print(my_list)  

my_list.pop(0)
print(my_list)