# Main program for logging temperature
import datetime, time 
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

                print ret
                readonserieport.read_temperature(serialport)
            serialport.close() 
