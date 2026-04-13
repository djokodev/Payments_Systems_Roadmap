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

def flat_fee(transaction):
    return 100  

def percentage_fee(transaction):
    return transaction["amount"] * 0.015

def apply_fee(transaction, fonction):

    fee = fonction(transaction)
    net_amount = transaction["amount"] - fee            

    return {
        "wallet_id": transaction["wallet_id"],
        "amount": transaction["amount"],
        "fee": fee,
        "net_amount": net_amount
    }  

def synthese_rapport_by_wallet(transactions):
    final_rapport = defaultdict(lambda: {"total": 0, "count": 0})

    for transaction in transactions:
        wallet = transaction["wallet_id"]
        final_rapport[wallet]["total"] += transaction["amount"]
        final_rapport[wallet]["count"] += 1

    return final_rapport


if __name__ == "__main__":
    
    result_of_synthese_rapport_by_wallet = synthese_rapport_by_wallet(transactions)
    print(result_of_synthese_rapport_by_wallet, end="\n")

    final_rapport_with_flat_fee = defaultdict(lambda: {"wallet_id": "", "amount": 0, "fee": 0.0, "net_amount": 0.0})
    final_rapport_percentage_fee = defaultdict(lambda: {"wallet_id": "", "amount": 0, "fee": 0.0, "net_amount": 0.0})

    for transaction in transactions:
        result_with_flat_fee = apply_fee(transaction, flat_fee)
        wallet = transaction["wallet_id"]
        final_rapport_with_flat_fee["wallet_id"] = result_with_flat_fee["wallet_id"]
        final_rapport_with_flat_fee[wallet]["amount"] += result_with_flat_fee["amount"]
        final_rapport_with_flat_fee[wallet]["fee"] += result_with_flat_fee["fee"]
        final_rapport_with_flat_fee[wallet]["net_amount"] += result_with_flat_fee["net_amount"]

    for transaction in transactions:
        result_with_percentage_fee = apply_fee(transaction, percentage_fee) 
        wallet = transaction["wallet_id"]
        final_rapport_percentage_fee["wallet_id"] = result_with_percentage_fee["wallet_id"]
        final_rapport_percentage_fee[wallet]["amount"] += result_with_percentage_fee["amount"]
        final_rapport_percentage_fee[wallet]["fee"] += result_with_percentage_fee["fee"]
        final_rapport_percentage_fee[wallet]["net_amount"] += result_with_percentage_fee["net_amount"]     

    print(final_rapport_with_flat_fee)
    print(final_rapport_percentage_fee)