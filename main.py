import time
import datetime
import webbrowser

def joinClasses(meetingInfo):
    while True:
        time.sleep(1)
        currentDate = datetime.datetime.now()
        currentDay = currentDate.strftime("%A")
        currentTime = currentDate.strftime(("%I:%M:%S %p"))

        print("Current Day: " + currentDay)
        print("Current time: " + currentTime)

        for i in meetingInfo:
            if i == currentDay:
                print("same day")
                for j in meetingInfo[i]:
                    print(j + ": j")
                    print(meetingInfo[i][j]+ ": meetingInfo[i][j]")
                    if currentTime == j:
                        print("same time")
                        webbrowser.open(meetingInfo[i][j])