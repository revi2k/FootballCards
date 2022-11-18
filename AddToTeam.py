import GenerateCard

class Team:
    def __init__ (self, name):
        self.name = name
        self.formation = { # There is only 4-2-2 formation already
            "GK":None,
            "LB":None,
            "CB1":None,
            "CB2":None,
            "RB":None,
            "CM1":None,
            "CM2":None,
            "CM3":None,
            "LW":None,
            "ST":None,
            "RW":None
        }
    def AddToTeam(self, position, card):
        self.formation[position] = card
    def ReturnTeam(self):
        print("Team: "+str(self.name)+" squad")
        for x in self.formation:
            print(x+"-"+str(self.formation[x]))
    def ShowStats(self):
        avPace = avShooting = avPassing = avDribbling = avDefence = avPhysicality = 0
        for player in self.formation:
            avPace += int((self.formation[player]["Pace"]))
            avShooting += int((self.formation[player]["Shooting"]))
            avPassing += int((self.formation[player]["Passing"]))
            avDribbling += int((self.formation[player]["Dribbling"]))
            avDefence += int((self.formation[player]["Defence"]))
            avPhysicality += int((self.formation[player]["Physicality"]))
        self.averageStats = {
            "Pace":int(avPace/11),
            "Shooting":int(avShooting/11),
            "Passing":int(avPassing/11),
            "Dribbling":int(avDribbling/11),
            "Defence":int(avDefence/11),
            "Physicality":int(avPhysicality/11)
        }
        print("Average "+str(self.name)+" stats\n"+str(self.averageStats))

Team1 = Team("TEAM")
Team1.AddToTeam("GK",GenerateCard.Card1.showCard())
Team1.AddToTeam("LB",GenerateCard.Card2.showCard())
Team1.AddToTeam("CB1",GenerateCard.Card3.showCard())
Team1.AddToTeam("CB2",GenerateCard.Card4.showCard())
Team1.AddToTeam("RB",GenerateCard.Card5.showCard())
Team1.AddToTeam("CM1",GenerateCard.Card6.showCard())
Team1.AddToTeam("CM2",GenerateCard.Card7.showCard())
Team1.AddToTeam("CM3",GenerateCard.Card8.showCard())
Team1.AddToTeam("LW",GenerateCard.Card9.showCard())
Team1.AddToTeam("ST",GenerateCard.Card10.showCard())
Team1.AddToTeam("RW",GenerateCard.Card11.showCard())

Team1.ReturnTeam()
Team1.ShowStats()
