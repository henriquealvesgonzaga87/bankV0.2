menu = '''1 - deposit
2 - withdraw
3 - statement
4 - exit
'''
balance_available = 0
total_withdraw = 500
NUMBER_WITHDRAW = 3
estatement = [[], []]
while True:
    print(menu)
    option = int(input('Choose one operation: '))
    if option == 1:
        deposit = float(input('type the amount: '))
        if deposit > 0:
            print(f'You deposited a total of {deposit:.2f} €')
            balance_available += deposit
            print(balance_available)
            estatement[0].append(deposit)
        else:
            print("Type a valid amount!")
    elif option == 2:
        if NUMBER_WITHDRAW == 0:
            print("You already achieved the maximum of 3 withdraws")
            continue
        if total_withdraw == 0:
            print('You achieved the maximum of 500.00 €')
            continue
        else:
            withdraw = float(input('Type the amount: '))
            if withdraw <= 0:
                print('This is not a valid amount!')
            elif withdraw > balance_available:
                print("You don't have this amount in your account.")
                print(balance_available)
                continue
            if withdraw > total_withdraw:
                print("The maximum allowed is 500.00 €")
            elif withdraw <= total_withdraw:
                if total_withdraw > 0:
                    NUMBER_WITHDRAW -= 1
                    total_withdraw -= withdraw
                    balance_available -= withdraw
                    print(balance_available)
                    estatement[1].append(withdraw)
                else:
                    print("You achieved the maximum of 500.00 €")
                    print(balance_available)
    elif option == 3:
        if len(estatement) == 0:
            print("You don't have any operations to show yet!")
        for i in estatement[0]:
            print(f"Deposit: {i} €")
        for i in estatement[1]:
            print(f"Withdraw: {i} €")
        print(f"Total availabe: {balance_available:.2f} €")
    elif option == 4:
        print('Thank you for being our client! See you soon!')
        break
    else:
        print('option invalid! Type a valid one')