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
        outcome = float(input('Type the amount: '))
        if outcome <= balance_available and NUMBER_WITHDRAW > 0:
            print(withdraw(value=outcome, statement=balance_available,
                           limit_withdraw=NUMBER_WITHDRAW, limit_amount=total_withdraw, register=estatement_list))
            balance_available -= outcome
    elif option == 3:
        if len(estatement_list) == 0:
            print("You don't have any operations to show yet!")
        for i in estatement_list[0]:
            print(f"Deposit: {i} €")
        for i in estatement_list[1]:
            print(f"Withdraw: {i} €")
        print(f"Total availabe: {balance_available:.2f} €")
    elif option == 4:
        print('Thank you for being our client! See you soon!')
        break
    else:
        print('option invalid! Type a valid one')