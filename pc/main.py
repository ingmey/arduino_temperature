# Main program for logging temperature
import datetime, time 
import checkPortConnect
import readonserieport
import serial
import sys

device = '/dev/ttyACM0'


if __name__ == "__main__":
    stored_exception = None
    while True:
        ret = checkPortConnect.check_presence(device)
        if ret:
            print "Arduino is connected "
            print "Setup serial port to Arduino"
            ser = serial.Serial()
            ser.port = device
            ser.baudrate = 9600
            ser.timeout = 5
            print "Wait 1,5 minutes for the Arduino"
            print "to connect to the serial port"
            time.sleep(90) # wait for port to be ready about 2 minutes
            try:
                ser.open()
                print "serial port has been open"
            except Expection, e: #serial.serialutil.SerialException
                print ("could not open serial port") + str(e)
                quit()
            today = datetime.datetime.now()
            todaydate1 =today.strftime("%Y-%m-%d")
            f = open('temperaturelog.txt', 'a')
            datestr = 'Date: ' + todaydate1 + '\n'
            print(datestr)
            f.write(datestr)
            while ser.is_open:
                try:
                    ser.flushInput()
                    ser.flushOutput()
                    time.sleep(5) # sleep 5 seconds
                    today = datetime.datetime.now()
                    todaydate2 =today.strftime("%Y-%m-%d")
                    if todaydate1 != todaydate2:
                        todaydate1 = todaydate2
                        print("Date: " + todaydate1)
                    ret = readonserieport.read_temperature(ser)
                    if ret:
                        print ret
                        f.write(ret)
                except (KeyboardInterrupt, SystemExit):
                    ser.close()
                    f.close()
                    quit()
                    
            ser.close()
            f.close()
