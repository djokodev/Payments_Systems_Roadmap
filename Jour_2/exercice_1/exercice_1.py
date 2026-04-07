from collections import defaultdict

transactions = [ 
    {"amount": 5000, "type": "send", "wallet_id": "CM_001"}, 
    {"amount": 15000, "type": "send", "wallet_id": "CM_002"}, 
    {"amount": 3000, "type": "receive", "wallet_id": "CM_001"}, 
    {"amount": 8000, "type": "send", "wallet_id": "CM_003"}, 
    {"amount": 20000, "type": "receive", "wallet_id": "CM_002"}, 
    {"amount": 1000, "type": "send", "wallet_id": "CM_001"}, 
    {"amount": 500, "type": "receive", "wallet_id": "CM_003"}, 
]


# Etape 1: Version avec une boucle for classique et setdefault
"""
def synthese_rapport_by_wallet(transactions):
    
    final_rapport = {}

    for transaction in transactions:
        final_rapport.setdefault(transaction["wallet_id"], 0)
        final_rapport[transaction["wallet_id"]] += transaction["amount"]

        
    print(final_rapport)


synthese_rapport_by_wallet(transactions)
"""


# Étape 2: Réécris avec defaultdict(int) depuis collections.
"""
def synthese_rapport_by_wallet(transactions):
    
    final_rapport = defaultdict(int)

    for transaction in transactions:
        final_rapport[transaction["wallet_id"]] += transaction["amount"]

        
    print(final_rapport)


synthese_rapport_by_wallet(transactions)
"""


# Étape 3: modifie ta fonction pour qu'elle retourne avec le nombre de transactions par wallet.
def synthese_rapport_by_wallet(transactions):
    final_rapport = defaultdict(lambda: {"total": 0, "count": 0})

    for transaction in transactions:
        wallet = transaction["wallet_id"]
        final_rapport[wallet]["total"] += transaction["amount"]
        final_rapport[wallet]["count"] += 1

    print(final_rapport)


synthese_rapport_by_wallet(transactions)
