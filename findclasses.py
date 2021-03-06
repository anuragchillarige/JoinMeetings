class readFile():
    def __init__(self):
        self.classesDict = {}

    def openAndReadFile(self):
        with open("meetings.txt", "r") as txtfile:
            for line in txtfile:
                timeMeeting = {}
                line = line.strip()

                day = line[0:line.index("|")].strip()
                time = line[line.index("|")+1:line.index("M") - 1].strip() + ":00 " + line[line.index("M")-1:line.rindex("|")]
                link = line[line.rindex("|") + 1:len(line)].strip()

                timeMeeting[time] = link
                self.classesDict[day] = timeMeeting

        txtfile.close()
        return self.classesDict
