# Read the temperature from a port
import serial, datetime, time
def read_temperature(ser):
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


