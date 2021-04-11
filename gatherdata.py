import datetime
import time
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
import findclasses
import webbrowser

link = ""
enteredTime = ""
day = ""


def addToFile(timeIn, linkIn, dayIn):
    with open("meetings.txt", "a") as file:
        file.write(dayIn + "|" + timeIn + "|" + linkIn + "\n")
        file.close()

def joinClasses(meetingInfo):
    while True:
        time.sleep(1)
        currentDate = datetime.datetime.now()
        currentDay = currentDate.strftime("%A")
        currentTime = currentDate.strftime(("%I:%M:%S"))


        """for i in meetingInfo:
            print("Current time: " + currentTime)
            print("Meeting time: " + i + "\n")
            if currentTime == i:
                print("Time for Meeting!")
                webbrowser.open(meetingInfo[i])"""

class MainScreen(Screen):

    def addMeeting(self):
        enteredTime = self.ids.time.text
        link = self.ids.link.text
        day = self.ids.day.text

        self.ids.time.text = ""
        self.ids.link.text = ""
        self.ids.day.text = ""

        addToFile(enteredTime, link, day)

    def finish(self):
        Window.close()
        allMeetingInfo = findclasses.readFile().openAndReadFile()

        joinClasses(allMeetingInfo)

class Instructions(Screen):
    pass

class ScreenMan(ScreenManager):
    pass

myFile = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return myFile


MainApp().run()
