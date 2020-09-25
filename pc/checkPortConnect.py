# check if device is connected
import serial.tools.list_ports

def check_presence(correct_port):
    myports = serial.tools.list_ports.comports()
    for port in myports:
        if port.device == correct_port:
            return True
    return False    

#if check_presence('/dev/ttyACM0'):
#    print "Arduino has been connected!"
#else: 
#    print "Arduino not connected!"
