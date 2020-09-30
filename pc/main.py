# Main program for logging temperature
import datetime, time 
import checkPortConnect
import serialportinit
import readonserieport
import signal
import sys

device = '/dev/ttyACM0'


if __name__ == "__main__":
    stored_exception = None
    while True:
        ret = checkPortConnect.check_presence(device)
        if ret:
            serialport = serialportinit.init_port(device)
            #time.sleep(2 * 60) # wait for port to b ready
            try:
                serialport.open()
                print "serial port open"
            except serial.serialutil.SerialException:
                print "could not open serial port open " + e
                quit()
            today = datetime.datetime.now()
            todaydate1 =today.strftime("%Y-%m-%d")
            print("Date: " + todaydate1)
            while serialport.is_open:
                time.sleep(5) # sleep 5 seconds
                today = datetime.datetime.now()
                todaydate2 =today.strftime("%Y-%m-%d")
                if todaydate1 != todaydate2:
                    todaydate1 = todaydate2
                    print("Date: " + todaydate1)
                ret = readonserieport.read_temperature(serialport)
                if ret:
                    print ret
            serialport.close()
