# Main program for logging temperature
import time 
import checkPortConnect
import serialportinit
import readonserieport

device = '/dev/ttyACM0'

if __name__ == "__main__":
    while True:
        ret = checkPortConnect.check_presence(device)
        if ret:
            serialport = serialportinit.init_port(device)
            try:
                serialport.open()
            except:
                print " error open serial port: " + str(e)
                exit()

            while serialport.is_open:
                readonserieport.read_temperature(serialport)
            serialport.close() 
