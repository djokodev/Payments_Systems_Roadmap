# une KeyError s'affichera dans la console de ce bloc de code car la cle 'c' n'existe pas pour le 'dic'
# dic = {'a': 1, 'b': 2}

# print("The value associated with 'c' is:")
# print(dic['c'])


# une mannier de gerer cette erreur est d'utiliser un defaultdict
# from collections import defaultdict

# dic_2 = defaultdict(lambda: "Key not found")

# dic_2["a"] = 1
# dic_2["b"] = 2

# print(dic_2["a"])
# print(dic_2["c"])
# print(dic_2)


# En utilisant get
# dic= {'India': '0091', 'Australia': '0025', 'Nepal': '00977'}

# print(dic.get('India', 'Not Found'))  
# print(dic.get('Japan', 'Not Found'))
# print(dic)


# En utilisant le block try, except
dic = {'India': '0091', 'Australia': '0025', 'Nepal': '00977'}
try:
    print(dic['India'])
    print(dic['USA'])
except KeyError:
    print('Not Found')