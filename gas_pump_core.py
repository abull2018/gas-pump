import gas_pump_disk
from gas_pump_disk import in_the_log


def gas_price(gas, amount):
    """ (str) -> float"""
    if gas == '1':
        return float(amount) * 1.17
    elif gas == '2':
        return float(amount) * 1.20
    elif gas == '3':
        return float(amount) * 2.50
    else:
        return None

def gas_type(gas):
    message = ''
    if gas == '1' or gas.lower() == 'one':
        gas_type = 'Regular'
    elif gas == '2' or gas.lower() == 'two':
        gas_type = 'Mid-grade'
    elif gas == '3' or gas.lower() == 'three':
        gas_type = 'Premium'
    return gas_type  

def revenue_log(left):
    # left = gas_pump_disk.in_the_log()
    price = 0
    for item in left:
        item[2] = float(item[2]) + float(item[2])
        price += item[2]
    return price

def refill(left):
    str_l = ['type, amount_in_tank, price']
    # left = gas_pump_disk.inside_tank()
    for item in left:
        if item[1] < 5000.0:
            item[1] = 5000.0
        item[1]=str(item[1])
        item[2]=str(item[2])
        str_l.append(', '.join(item))
    message = '\n'.join(str_l)

        
