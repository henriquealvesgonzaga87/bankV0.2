def deposit(value, statement):
    if value > 0:
        statement[0].append(value)
        return f'You deposited a total of {value:.2f} €'
    else:
        return "Type a valid amount!"


def limit_total_withdraw():
    return "You already achieved the maximum of 3 withdraws"


def limit_amount_withdraw():
    return "You achieved the maximum of 500.00 €"


def more_than_maximun_allowed():
    return "The maximum allowed is 500.00 €"


def less_than_available():
    return "You don't have this amount in your account."


def less_than_zero():
    return 'This is not a valid amount!'


def withdraw(*, value, statement, limit_amount, limit_withdraw, register):
    limit_withdraw -= 1
    limit_amount -= value
    statement -= value
    register[1].append(value)
    return statement


def statement_account(available, *, summary):
    if len(summary) == 0:
        print("You don't have any operations to show yet!")
    for i in summary[0]:
        print(f"Deposit: {i:.2f} €")
    for i in summary[1]:
        print(f"Withdraw: {i:.2f} €")
    print(f"Total availabe: {available:.2f} €")
