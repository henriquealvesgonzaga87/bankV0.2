def deposit(value, statement):
    if value > 0:
        statement[0].append(value)
        return f'You deposited a total of {value:.2f} €'
    else:
        return "Type a valid amount!"


def withdraw(*, value, statement, limit_amount, limit_withdraw, register):
    #dividir em várias funções para cada caso diferente
    if limit_withdraw == 0:
        return "You already achieved the maximum of 3 withdraws"
    if limit_amount == 0:
        return 'You achieved the maximum of 500.00 €'
    if value <= 0:
        return 'This is not a valid amount!'
    if value > limit_amount:
        return "The maximum allowed is 500.00 €"
    if value > statement:
        print("You don't have this amount in your account.")
        return statement
    if value <= limit_amount:
        if limit_amount > 0:
            limit_withdraw -= 1
            limit_amount -= value
            statement -= value
            register[1].append(value)
            return statement
        else:
            print("You achieved the maximum of 500.00 €")
            return statement
