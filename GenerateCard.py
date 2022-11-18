import random

class FootballCard:
    def __init__(self, surname, overall):
        self.surname = surname
        self.overall = overall
        self.generateStats()
    def generateStats(self):
        self.cardStats = {
            "Pace":None,
            "Shooting":None,
            "Passing":None,
            "Dribbling":None,
            "Defence":None,
            "Physicality":None
        }
        for stat in self.cardStats:
            self.cardStats[stat] = random.randrange(self.overall-10,self.overall+10)

    def showCard(self):
        return self.cardStats

#CREATING 11 CARDS#

Card1 = FootballCard("Card1", 93)
Card2 = FootballCard("Card2", 90)
Card3 = FootballCard("Card3", 78)
Card4 = FootballCard("Card4", 83)
Card5 = FootballCard("Card5", 85)
Card6 = FootballCard("Card6", 87)
Card7 = FootballCard("Card7", 77)
Card8 = FootballCard("Card8", 64)
Card9 = FootballCard("Card9", 91)
Card10 = FootballCard("Card10", 80)
Card11 = FootballCard("Card11", 79)


