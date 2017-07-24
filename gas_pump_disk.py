import core

message = ''
    if gas == '1':
        gas_type = 'Regular'
    elif gas == '2':
        gas_type = 'Mid-grade'
    elif gas == '3':
        gas_type = 'Premium'

message = '\n{}, {}, {}'.format(gas_type, amount, price)
    with open('log.txt', 'a') as file:
        file.write(message)