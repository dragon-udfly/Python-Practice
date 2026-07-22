voltage_pin1 = 23.2
voltage_pin2 = 32.3
excess_voltage = 0

if voltage_pin1 > voltage_pin2:
    excess_voltage = voltage_pin1 - voltage_pin2
elif voltage_pin2 > voltage_pin1:
    excess_voltage = voltage_pin2 - voltage_pin1

print(f"Voltage Pin 1: {voltage_pin1}\nVoltage Pin 2: {voltage_pin2}\nExcess Voltage: {excess_voltage}")