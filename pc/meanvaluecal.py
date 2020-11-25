import datetime, time

def calcMeanValue(tempList):
    N = 10
    sum = 0.0
    average = 0
    dt = datetime.datetime.now()
    timestr = dt.strftime("%H:%M")
    for x in tempList:
        sum = sum + x
    average = sum / N
    return "time: " + timestr + " temperature " + str(average)
    
