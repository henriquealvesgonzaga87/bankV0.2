from functions import *
from account import *
menu = '''1 - register client
2 - deposit
3 - withdraw
4 - statement
5 - exit
'''
balance_available = 0
total_withdraw = 500
NUMBER_WITHDRAW = 3
estatement_list = [[], []]
tax_number_register = []
client_register = []
all_clients = []
data_account = []
account_number = 1
AGENCY_NUMBER = "0001"
while True:
    print(menu)
    option = int(input('Choose one operation: '))
    if option == 1:
        print('Registering Client')
        test_tax_number = int(input('Tax Number (numbers only): '))
        if test_tax_number not in tax_number_register:
            tax_number_register.append(test_tax_number)
            client_register.append(test_tax_number)
            client_data = register_client(client=client_register)
            client_register.append(client_data)
            account = create_account(n_account=account_number, n_agency=AGENCY_NUMBER)
            client_register.append(account)
            all_clients.append(client_register)
            account_number += 1
            continue
        else:
            print('Already registered')
            create_another_account = str(input("Do you wanna create another account? [Y/N]: ")).strip().upper()
            if create_another_account not in 'yYnN':
                create_another_account = str(input("Do you wanna create another account? [Y/N]: ")).strip().upper()
            else:
                if create_another_account == 'Y':
                    another_account = create_account(n_account=account_number, n_agency=AGENCY_NUMBER)
                    all_clients.append(another_account)
                    account_number += 1
                    client_register.clear()
                    continue
                else:
                    client_register.clear()
                    continue
    if option == 2:
        income = float(input('type the amount: '))
        print(deposit(income, estatement_list))
        balance_available += income
        continue
    elif option == 3:
        outcome = int(input('Type how much for the withdraw: '))
        if NUMBER_WITHDRAW == 0:
            print(limit_total_withdraw())
            continue
        if total_withdraw == 0:
            print(limit_amount_withdraw())
            continue
        if outcome > 500:
            print(more_than_maximun_allowed())
            continue
        if outcome > balance_available:
            print(less_than_available())
            continue
        if outcome <= 0:
            print(less_than_zero())
            continue
        else:
            if outcome <= total_withdraw:
                if total_withdraw > 0:
                    accepted_withdraw = withdraw(value=outcome, statement=balance_available,
                                                 limit_amount=total_withdraw, limit_withdraw=NUMBER_WITHDRAW,
                                                 register=estatement_list)
                    balance_available -= outcome
                    total_withdraw -= outcome
                    NUMBER_WITHDRAW -= 1
                else:
                    print(limit_amount_withdraw())
            continue
    elif option == 4:
        statement_account(balance_available, summary=estatement_list)
    elif option == 5:
        print('Thank you for being our client! See you soon!')
        break
    else:
        print('option invalid! Type a valid one')
