"""
This module implements different bank account types based on an abstract AccountManager class,
following the Factory design pattern to encapsulate the creation logic of accounts.

The Factory pattern decouples the client code from the concrete implementations,
promoting scalability and adherence to SOLID principles.

Implemented account types include: SavingsAccount, CheckingAccount, and CreditAccount.
"""

from accounts.factory import AccountFactory
from cards.factory import CardFactory

def main():
    # --- FASE 1: PREPARACIÓN DEL ENTORNO (El banco crea los datos) ---
    # Esto no lo hace el usuario en el cajero, es el estado inicial del sistema.
    
    print("Configurando el entorno del banco...")
    account_factory = AccountFactory()
    card_factory = CardFactory()

    # Creamos una cuenta de ahorros con 1000€
    savings_account_1 = account_factory.create_account(
        "savings", 
        account_holder="Christian Marzal", 
        balance=1000
    )

    # Creamos una tarjeta de débito asociada a esa cuenta
    debit_card_1 = card_factory.create_card(
        "debit", 
        card_number="1234-5678-9012-3456", 
        pin="1234", 
        linked_account=savings_account_1
    )
    print("Entorno listo.\n")


    # --- FASE 2: SIMULACIÓN DEL CAJERO AUTOMÁTICO ---
    # El usuario "introduce" la tarjeta en el cajero.
    
    print("Bienvenido al ATM. Por favor, inserte su tarjeta.")
    # (Aquí simularíamos la inserción de debit_card_1)
    
    pin_introducido = input("Introduzca su PIN: ")

    if debit_card_1.validate_pin(pin_introducido):
        print("PIN correcto.")
        
        # El cajero opera con la cuenta asociada
        cuenta_actual = debit_card_1.get_account()
        print(f"Saldo actual: {cuenta_actual.get_balance()}€")
        
        try:
            cantidad_a_retirar = float(input("Introduzca la cantidad a retirar: "))
            print(f"Retirando {cantidad_a_retirar}€...")
            cuenta_actual.withdraw(cantidad_a_retirar)
            print(f"Nuevo saldo: {cuenta_actual.get_balance()}€")
        except ValueError as e:
            print(f"Error: {e}")
        
    else:
        print("PIN incorrecto.")

if __name__ == "__main__":
    main()






