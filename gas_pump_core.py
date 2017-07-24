import gas_pump_disk

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

def gas_type(gas_price):
    message = ''
    if gas == '1':
        gas_type = 'Regular'
    elif gas == '2':
        gas_type = 'Mid-grade'
    elif gas == '3':
        gas_type = 'Premium'
        



def revenue_log():
    left = in_the_log()
    price = 0
    for item in left:
        item[2] = float(item[2]) + float(item[2])
        price += item[2]
    return price

def refill():
    str_l = ['type, amount_in_tank, price']
    left = inside_tank()
    for item in left:
        if item[1] < 5000.0:
            item[1] = 5000.0
        item[1]=str(item[1])
        item[2]=str(item[2])
        str_l.append(', '.join(item))
    message = '\n'.join(str_l)

        
