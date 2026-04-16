import functools
import time


def log_execution(func):
    @functools.wraps(func)
    def wrapper_log_execution(*args, **kwargs):

        print(f"le nom de la fonction est {func.__name__}")
        print(f"les arguments de la fonction sont `args={args}` et `kwargs={kwargs}`")

        t1 = time.time()
        result_of_func = func(*args, **kwargs)
        t2 = time.time()

        t = t2 - t1

        print(f"le temps d'execution de la fonction est de {t}s")

        return result_of_func


def retry(max_attempts):
    def decorator_of_retry(func):
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except:
                    print(f"tentative {i} échouée")

            return wrapper_retry
        return decorator_of_retry



def validate_amount(func):
    """
    Décorateur qui valide le montant d'une transaction avant d'exécuter la fonction.

    Convention obligatoire : 'amount' doit toujours être passé comme
    premier argument positionnel de la fonction décorée.
    Exemple valide   : send_money(50000, wallet_id="CM_001")
    Exemple invalide : send_money(wallet_id="CM_001", amount=50000)

    Règles de validation :
    - amount doit être strictement positif (> 0)
    - amount doit être strictement inférieur à 2 000 000 FCFA
    
    Lève une ValueError si l'une des conditions n'est pas respectée.
    """
    @functools.wraps(func)
    def wrapper_validate_amount(*args, **kwargs):
        amount = args[0]

        if amount <= 0:
            raise ValueError(
                f"Montant invalide : {amount} FCFA. "
                f"Le montant doit être strictement positif."
            )
        if amount >= 2_000_000:
            raise ValueError(
                f"Montant invalide : {amount} FCFA. "
                f"Le montant dépasse la limite de 2 000 000 FCFA."
            )

        return func(*args, **kwargs)

    return wrapper_validate_amount