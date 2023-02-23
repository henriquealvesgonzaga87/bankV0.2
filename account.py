def register_client(*, client):
    client = []
    address = {}
    name = str(input('Name: ')).strip().title()
    birth_day = str(input('Birth Day (yyyy/mm/dd): ')).strip()
    address['street'] = str(input('Street: ')).strip().title()
    address['number'] = str(input('Number: ')).strip()
    address['neighborhood'] = str(input('Neighborhood: ')).strip().title()
    address['city'] = str(input('City: ')).strip().title()
    address['state'] = str(input('State: ')).strip().upper()
    client.append(name)
    client.append(birth_day)
    client.append(address)
    return client


def create_account(*, n_account, n_agency):
    data_account = [n_account, n_agency]
    return data_account
