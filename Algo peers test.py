# Question 1
# WRITE A FUNCTION TO CALCUATE THE VOLTAGE READINGS FROM A SOLAR PANEL.
vref = 3.3
adc_resolution = 65535
raw_value = 73.2
 
def voltage_function():
    voltage = (raw_value/adc_resolution) * vref
    return voltage

volts = voltage_function()
print (f"Voltage:{volts:.2f}")

# Question 2
raw_value1 = 0.03
raw_value2 = 8.10
raw_value3 = 9.997
raw_value4 = 1010.1
raw_value5 = 0.003


def voltage_function2():
    float_changer1 = (raw_value1/adc_resolution) * vref
    float_changer2 = (raw_value2/adc_resolution) * vref
    float_changer3 = (raw_value3/adc_resolution) * vref
    float_changer4 = (raw_value4/adc_resolution) * vref
    float_changer5 = (raw_value5/adc_resolution) * vref
    print (f"Values:{float_changer1:.2f}")
    print (f"Values:{float_changer2:.2f}")
    print (f"Values:{float_changer3:.2f}")
    print (f"Values:{float_changer4:.2f}")
    print (f"Values:{float_changer5:.2f}")
    
    return float_changer1, float_changer2, float_changer3, float_changer4, float_changer5

volts_float = voltage_function2()
