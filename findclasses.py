class readFile():
    def __init__(self):
        self.classesDict = {}

    def openAndReadFile(self):
        with open("meetings.txt", "r") as txtfile:
            for line in txtfile:
                line = line.strip()

                time = line[0 : line.index("|")]
                link = line[line.index("|") + 1 : len(line)]

                self.classesDict[time] = link

        return self.classesDict
readFile().openAndReadFile()