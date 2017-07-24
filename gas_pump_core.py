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

def gas_type(gas):
    message = ''
    if gas == '1':
        gas_type = 'Regular'
    elif gas == '2':
        gas_type = 'Mid-grade'
    elif gas == '3':
        gas_type = 'Premium'




def keep_log(gas, amount):
    price = gas_price(gas, amount)

def revenue_log():
    left = in_the_log()
    price = 0
    for item in left:
        item[2] = float(item[2]) + float(item[2])
        price += item[2]
    return price
    
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

        
