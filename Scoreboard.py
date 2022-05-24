class Scoreboard:
    def __init__(self):
        self.__scoreboard = {}
        self.FillTheScoreboard
    def FillTheScoreboard(self):
        file = open("scores.txt", "r")
        content = file.read()
        file.close()
        list_content = content.split(" ")

        slownik = {}

        i = 0
        while i < len(list_content):
            slownik[list_content[i]] = int(list_content[i + 1])
            i += 2
        print(slownik)

    def Display(self):
        for key in self.__scoreboard:
            print(key + " " + str(self.__scoreboard[key]))

