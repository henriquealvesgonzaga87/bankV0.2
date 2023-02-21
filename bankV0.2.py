from functions import *
menu = '''1 - deposit
2 - withdraw
3 - statement
4 - exit
'''
balance_available = 0
total_withdraw = 500
NUMBER_WITHDRAW = 3
estatement_list = [[], []]
while True:
    print(menu)
    option = int(input('Choose one operation: '))
    if option == 1:
        income = float(input('type the amount: '))
        print(deposit(income, estatement_list))
        balance_available += income
        continue
    elif option == 2:
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
                    print(total_withdraw)
                else:
                    print(limit_amount_withdraw())
            continue
    elif option == 3:
        statement_account(balance_available, summary=estatement_list)
    elif option == 4:
        print('Thank you for being our client! See you soon!')
        break
    else:
        print('option invalid! Type a valid one')