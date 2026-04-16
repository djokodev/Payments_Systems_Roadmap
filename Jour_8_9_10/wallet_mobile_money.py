class WalletMobileMoney:
    
    def __init__(self, wallet_id, owner_name, phone, balance, kyc_level, is_blocked=False):
        self.wallet_id = wallet_id
        self.owner_name = owner_name
        self.phone = phone
        self._balance = balance
        self.kyc_level = kyc_level
        self.is_blocked = is_blocked    

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Le solde ne peut pas être négatif")
        self._balance = value

    def credit(self, amount):
        if self.is_blocked:
            raise ValueError("Votre compte a été bloqué.")
        if amount <= 0:
            raise ValueError("Le montant ne peut pas etre negatif ou null")
        self._balance += amount

    def debit(self, amount):
        if self.is_blocked:
            raise ValueError("Votre compte a été bloqué.")
        if amount <= 0:
            raise ValueError("Le montant ne peut pas etre negatif ou null")
        if amount > self._balance:
            raise ValueError("Votre solde est insuffisant")
        self._balance -= amount

    def get_daily_limit(self):
        LIMITS = {1: 100_000, 2: 500_000, 3: 2_000_000}
        return LIMITS.get(self.kyc_level, 0)
    
        
    def __str__(self):
        return f"Compte {self.wallet_id} de {self.owner_name}, votre solde est de {self._balance}XAF | KYC : {self.kyc_level} |  Status : {self.is_blocked}"
    
    def __repr__(self):
        return f"MobileMoneyAccount (id='{self.wallet_id}', name='{self.owner_name}', phone='{self.phone}', balance='{self._balance}')"
    
    def __eq__(self, other):
        return self.wallet_id == other.wallet_id
    


if __name__ == "__main__":
    wallet = WalletMobileMoney(wallet_id="O1", owner_name="Djoko", phone=652260368, balance=0, kyc_level=1)
    print(wallet)

    wallet.credit(500)
    print(wallet.balance)

    wallet.debit(100)
    print(wallet.balance)

    try:
        wallet.debit(1000)
    except Exception as e:
        print(e)

    wallet.is_blocked = True

    try:
        wallet.credit(100)
    except Exception as e:
        print(e)

    try:
        wallet.debit(100)
    except Exception as e:
        print(e)

    for i in [1,2,3]:
        wallet_test_limit = WalletMobileMoney("TEST", "Test", 600000000, 0, i)
        print(wallet_test_limit.get_daily_limit())
        
    w1 = WalletMobileMoney("O1", "Djoko", 652260368, 0, 1)
    w2 = WalletMobileMoney("O1", "Autre", 699000000, 5000, 2)
    print(w1 == w2) 

    w3 = WalletMobileMoney("O2", "simo", 677000000, 0, 1)
    print(w1 == w3)
    