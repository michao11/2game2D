class Scoreboard:
    def __init__(self):
        self.__scoreboard = {}
        self.FillTheScoreboard

    def FillTheScoreboard(self):
        file = open("scores.txt", "r")
        content = file.read()
        content = content[:-1]
        file.close()

        list_content = content.split(" ")

        i = 0
        while i < len(list_content):
            self.__scoreboard[list_content[i]] = int(list_content[i + 1])
            i += 2

    def Display(self):
        for key in self.__scoreboard:
            print(key + " " + str(self.__scoreboard[key]))

    def Save(self, p_name, p_points):
        if p_name in self.__scoreboard:
            if self.__scoreboard[p_name] < p_points:
                self.__scoreboard[p_name] = p_points
        else:
            self.__scoreboard[p_name] = p_points

        file = open("scores.txt", 'w')
        for key in self.__scoreboard:
            file.write(key + " " + str(self.__scoreboard[key]) + " ")
        file.close()
