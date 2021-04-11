import time
import datetime
import webbrowser

def joinClasses(meetingInfo):
    while True:
        time.sleep(1)
        currentDate = datetime.datetime.now()
        currentDay = currentDate.strftime("%A")
        currentTime = currentDate.strftime(("%I:%M:%S %p"))

        for i in meetingInfo:
            if i == currentDay:
                for j in meetingInfo[i]:
                    if currentTime == j:
                        print("Time for meeting!")
                        webbrowser.open(meetingInfo[i][j])