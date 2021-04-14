from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
import findclasses
import main

link = ""
enteredTime = ""
day = ""

def addToFile(timeIn, linkIn, dayIn):
    with open("meetings.txt", "a") as file:
        file.write(dayIn + "|" + timeIn + "|" + linkIn + "\n")
        file.close()

class MainScreen(Screen):

    def addMeeting(self):
        enteredTime = self.ids.time.text.strip()
        link = self.ids.link.text.strip()
        day = self.ids.day.text.strip()

        errorMessage = ""

        self.ids.time.text = ""
        self.ids.link.text = ""
        self.ids.day.text = ""

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        validDay = False
        for x in days:
            if day == x:
                validDay = True
                break

        if len(enteredTime) != 8 or enteredTime.index(":") == -1 or int(enteredTime[0:enteredTime.index(":")]) > 12:
            errorMessage += "Invalid time!\n"

        elif not validDay:
            errorMessage += "Invalid day!\n"

        else:
            addToFile(enteredTime, link, day)

        self.ids.messageLabel.text = errorMessage

    def finish(self):
        Window.close()
        allMeetingInfo = findclasses.readFile().openAndReadFile()

        main.joinClasses(allMeetingInfo)

class Instructions(Screen):
    pass

class ViewMeetingsScreen(Screen):
    def listMeetings(self):
        allMeetings = ""
        meetingDays = []

        try:
            with open("meetings.txt", "r") as file:
                for i in file:
                    sameDay = False
                    i = i[0:i.index("|")]
                    for j in meetingDays:
                        if i == j:
                            sameDay = True
                            break

                    if not sameDay:
                        meetingDays.append(i)
            file.close()

            for x in meetingDays:
                allMeetings += x + "\n"

                with open("meetings.txt", "r") as file:

                    for y in file:
                        if y[0:y.index("|")] == x:
                            dayAndLink = y[y.index("|") + 1:y.rindex("|")] + ": " + y[y.rindex("|") + 1:len(y)]
                            allMeetings += dayAndLink

                    allMeetings += "\n"

                file.close()

        except FileNotFoundError:
            allMeetings = "File not found."

        return allMeetings

        return allMeetingsIn

class RemoveMeetingsScreen(Screen):
    pass

class ScreenMan(ScreenManager):
    pass

myFile = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return myFile


MainApp().run()
