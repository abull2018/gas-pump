import gas_pump_core
import gas_pump_disk

def main():
    msg = '''Welcome to Lane Station!! What type of gas would you like to purchase?\n
    \t1. Regular.$1.17\n
    \t2. Mid-grade.$1.20\n
    \t3. Premium.$2.50\n
    '''
    while True:
        gas = input(msg)
        if gas.lower() == 'refuel':
            gas_pump_core.refill()
            print('Thanks refueled.')
            return None
        if gas.lower() == 'revenue':
            print('your total revenue is ${:.2f}'.format(gas_pump_core.revenue_log()))
            return None
        if gas == '1' or gas == '2' or gas == '3':
            break 
        else:
            print('Sorry invalid choice!')
    amount = input('How many gallons would you like?\n')
    print('Your total will be ${:.2F}'.format(gas_pump_core.gas_price(gas, amount)))

    gas_type = gas_pump_disk.keep_log(gas, amount)        
    gas_pump_disk.take_away(gas_type, amount)
    print('Thank you, Have a Nice Day ;) !')

if __name__ == '__main__': 
    main()

    