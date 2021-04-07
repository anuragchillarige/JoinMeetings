import datetime
import time
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import findclasses
import webbrowser

link = ""
time = ""


def addToFile(timeIn, linkIn):
    with open("meetings.txt", "a") as file:
        file.write(timeIn + "|" + linkIn + "\n")
        file.close()

def joinClasses(meetingInfo):
    while True:
        time.sleep(1)
        currentDate = datetime.datetime.now()
        currentDay = currentDate.strftime("%a")
        currentTime = currentDate.strftime(("%I:%M:%S"))

        for i in meetingInfo:
            if currentTime == meetingInfo[i]:
                print("Time for a meeting!!")

class MainScreen(Screen):

    def addMeeting(self):
        enteredTime = self.ids.time.text
        link = self.ids.link.text

        addToFile(enteredTime, link)

    def finish(self):
        Window.close()
        print("Window closed")
        allMeetingInfo = findclasses.readFile().openAndReadFile()

        joinClasses(allMeetingInfo)


class MainApp(App):

    def build(self):
        return MainScreen()


MainApp().run()
