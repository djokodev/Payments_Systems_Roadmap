Contexte : Tu es backend developer chez une fintech camerounaise. Le système reçoit en fin de journée la liste brute de toutes les transactions traitées. Ta fonction doit produire un rapport de synthèse par wallet.


Données d'entrée :

`transactions = [
    {"amount": 5000,  "type": "send",    "wallet_id": "CM_001"},
    {"amount": 15000, "type": "send",    "wallet_id": "CM_002"},
    {"amount": 3000,  "type": "receive", "wallet_id": "CM_001"},
    {"amount": 8000,  "type": "send",    "wallet_id": "CM_003"},
    {"amount": 20000, "type": "receive", "wallet_id": "CM_002"},
    {"amount": 1000,  "type": "send",    "wallet_id": "CM_001"},
    {"amount": 500,   "type": "receive", "wallet_id": "CM_003"},
]`


Ce que ta fonction doit retourner :

`python {
    "CM_001": 9000,
    "CM_002": 35000,
    "CM_003": 8500,
}`