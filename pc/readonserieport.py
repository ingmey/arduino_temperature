# Read the temperature from ser port
import serial
import time

def read_temperature(ser):
    ser.write(b"te\n")
    time.sleep(1) # wait for response 1 seconds
    response  = ser.readline()
    if(response.strip() != 'yes'):
        return float(response)
