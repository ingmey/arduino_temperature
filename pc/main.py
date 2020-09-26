# Main program for logging temperature
import time 
import checkPortConnect
import serialportinit
import readonserieport

device = '/dev/ttyACM0'

if __name__ == "__main__":
    serialportopen = False
    while True:
        ret = checkPortConnect.check_presence(device)
        if ret:
            serialport = serialportinit.init_port(device)
            try:
                serialport.open()
                serialportopen = True
            except:
                print " error open serial port: " + str(e)
                exit()
            print ret
            while serialport.is_open:
                time.sleep(5) # sleep 5 seconds
                print ret
                readonserieport.read_temperature(serialport)
            serialport.close() 
