import serial,time
#initialization and open the port
ser = serial.Serial()
ser.port = "/dev/ttyACM0"
ser.baudrate = 9600
ser.timeout = 5               #non-block read
#ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control

try: 
    ser.open()

except Exception, e:
    print "error open serial port: " + str(e)
    exit()

while ser.isOpen():
    read_data = ser.read(20)
   # response  = ser.readline()
    print"Data received : " + read_data

#else:
#    print "Can not open serial port"
