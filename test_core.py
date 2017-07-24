import gas_pump_core

def test_gas_price():
    assert gas_pump_core.gas_price('2', 25) == 30.0
    assert gas_pump_core.gas_price('3', 5) == 12.5
    assert gas_pump_core.gas_price('1', 10) == 11.7
    assert gas_pump_core.gas_price('1', 10) == 11.7

# def test_keep_log():
#     assert gas_pump_core.keep_log('2', 25) == 30.0
#     assert gas_pump_core.keep_log('3', 5) == 12.5
#     assert gas_pump_core.keep_log('1', 10) == 11.7
#     assert gas_pump_core.keep_log('3', 15) == 37.5
