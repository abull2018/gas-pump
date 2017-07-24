import gas_pump_core

def test_gas_price():
    assert gas_pump_core.gas_price('2', 25) == 30.0
    assert gas_pump_core.gas_price('3', 5) == 12.5
    assert gas_pump_core.gas_price('1', 10) == 11.7
    assert gas_pump_core.gas_price('1', 10) == 11.7

def test_gas_type():
    assert gas_pump_core.gas_type('1') == 'Regular'
    assert gas_pump_core.gas_type('one') == 'Regular'    
    assert gas_pump_core.gas_type('3') == 'Premium'
    assert gas_pump_core.gas_type('three') == 'Premium'
    assert gas_pump_core.gas_type('2') == 'Mid-grade'
    assert gas_pump_core.gas_type('two') == 'Mid-grade'


# def test_revenue_log():
#     assert gas_pump_core.revenue_log(left) == price



