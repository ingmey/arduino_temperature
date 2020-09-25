# Read the temperature from a port
import serial, datetime, time
def init_port(port):
    #initialization and open the port
    ser = serial.Serial()
    ser.port = port
    ser.baudrate = 9600
    ser.timeout = 5               #non-block read
    #ser.timeout = 2              #timeout block read
    ser.xonxoff = False     #disable software flow control
    ser.rtscts = False     #disable hardware (RTS/CTS) flow control
    ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
    return ser;

