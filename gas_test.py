import gas_pump_core

def gas_price():
    assert gas_price(2) == 1.20
    assert gas_price(3) == 2.50
    assert gas_price(1) == 1.17
