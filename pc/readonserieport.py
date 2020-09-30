# Read the temperature from ser port
import serial
import datetime, time

def read_temperature(ser):
    ser.write(b"te\n")
    dt = datetime.datetime.now()
    time.sleep(1) # wait for response 1 seconds
    response  = ser.readline()
    responsecheck = response.strip()
    if(response.strip() != 'yes'):
        return "time: " + dt.strftime("%H:%M") + " temperature: %s" % response
