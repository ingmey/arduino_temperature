# Main program for logging temperature
import ConfigParser
import datetime, time 
import checkPortConnect
import readonserieport
import serial
import sys


if __name__ == "__main__":
    # read config parameters
    cfg = ConfigParser.ConfigParser()
    cfg.read('temperaturemeasureconfig.cfg')
    device = cfg.get('Section1', 'device')
    file_name_end = cfg.get('Section1', 'Filename')
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
            current_date_and_time = datetime.datetime.now()
            current_date = current_date_and_time.strftime("%Y%m%d")
            file_name = str(current_date) + file_name_end
            f = open(file_name, 'a')
            datestr = 'Date: ' + current_date + '\n'
            print(datestr)
            f.write(datestr)
            while ser.is_open:
                try:
                    ser.flushInput()
                    ser.flushOutput()
                    time.sleep(5) # sleep 5 seconds
                    current_date_and_time = datetime.datetime.now()
                    current_date2 = current_date_and_time.strftime("%Y%m%d")
                    if current_date !=  current_date2:
                        f.close()
                        current_date =  current_date2
                        file_name = str(current_date) + file_name_end
                        f = open(file_name, 'a')
                        print("Date: " + current_date)
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
