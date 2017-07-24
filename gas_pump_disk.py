import gas_pump_core
# from gas_pump_core import gas_price
# message = '\n{}, {}, {}'.format(amount, price)
# with open('log.txt', 'a') as file:
def keep_log(gas, amount):
    price = gas_pump_core.gas_price(gas, amount)

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



def in_the_log():
    left =[]
    with open('log.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2].replace('$', ''))])
    return left

def inside_tank():
    left = []
    with open('tank.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2])])
    return left

def take_away(gas_type, amount):
    str_l = ['type, amount_in_tank, price']
    left = inside_tank()
    for item in left:
        if item[0] == gas_type:
            if float(amount) > item[1]:
                print('Sorry Max amount reached! We only have 5000.0 gallons.')
            else:
                item[1] = float(item[1]) - float(amount)
        item[1] = str(item[1])
        item[2] = str(item[2])
        str_l.append(', '.join(item))
    message = '\n'.join(str_l)
    with open('tank.txt', 'w') as file:
        file.write(message)



