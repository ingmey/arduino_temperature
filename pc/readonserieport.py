# Read the temperature from a port
import serial
import datetime, time

def read_temperature(ser):
    ser.write(b"te\n")
    dt = datetime.datetime.now()
    time.sleep(1) # wait for response 1 seconds
    response  = ser.readline()
    print("time: " + dt.strftime("%H:%M") + " temperature: %s" % response)


