#!/usr/bin/python
import serial, datetime, time

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
today = datetime.datetime.now()
todaydate1 =today.strftime("%Y-%m-%d")
print("Date: " + todaydate1)
while ser.isOpen():
    today = datetime.datetime.now()

    todaydate2 =today.strftime("%Y-%m-%d")
    if todaydate1 != todaydate2:
        todaydate1 = todaydate2
        print("Date: " + todaydate1)
    ser.write(b"te\n")
    dt = datetime.datetime.now()
    response  = ser.readline()
    print("time: " + dt.strftime("%H:%M") + " temperature: %s" % response)
    time.sleep(30) # sleep 30 seconds

