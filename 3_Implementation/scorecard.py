class player:
    odiruns=0
    list = ["Yuvi", "Dhoni", "virat", "stokes", "boult", "starc", "jonny", "abd"]
    def scorecard(self,name):
        self.name = name
        self.odiruns = odiruns
        list = ["Yuvi", "Dhoni", "virat", "stokes", "boult", "starc", "jonny", "abd"]
        if name in list:
            print("name is found his name is", name)
        else:
            print("name not found")

    def cricket(self, name):
        if name == "Yuvi":
            print("century=20")
            print("wickets=300")
            print("odiruns=10000")
            print("test runs=12000")
            print("strikerate=120.0")
            print("average=60.0")
        elif name == "Dhoni":
            print("century=15")
            print("wickets=0")
            print("odiruns=7000")
            odiruns=7000
            print("test runs=2000")
            print("strikerate=150.0")
            print("average=40.0")
        elif name == "virat":
            print("century=15")
            print("wickets=0")
            print("odiruns=7000")
            odiruns=7000
            print("test runs=2000")
            print("strikerate=150.0")
            print("average=40.0")
        elif name == "stokes":
            print("century=15")
            print("wickets=0")
            print("odiruns=7000")
            odiruns=7000
            print("test runs=2000")
            print("strikerate=150.0")
            print("average=40.0")
        elif name == "starc":
            print("century=15")
            print("wickets=500")
            print("odiruns=1000")
            odiruns=1000
            print("test runs=2000")
            print("strikerate=170.0")
            print("average=20.0")
        elif name == "jonny":
            print("century=5")
            print("wickets=0")
            print("odiruns=5000")
            odiruns=5000
            print("test runs=8000")
            print("strikerate=150.0")
            print("average=30.0")
        elif name == "abd":
            print("century=24")
            print("wickets=30")
            print("odiruns=11000")
            odiruns=11000
            print("test runs=15000")
            print("strikerate=200.0")
            print("average=70.0")
class team(player):
    list1=[]
    list2=[]
    def team(self):
        if odiruns>=150:
            if name in player.list:
                team.list1.append(name)
                print("team A", team.list1)

        elif odiruns<150:
            if name in player.list:
                team.list2.append(name)
                print("team B", team.list2)


obj = team()
x=False
while x==False:
    e=input("type 'y' of you want to make team \n press 'n' if you want to quit \n press 'l' if you want to print list and quit")

    if e=='y':
            name = input("enter the name")
            try:
                odiruns = int(input("enter odi runs"))
                obj.scorecard(name)
                obj.cricket(name)
                obj.team()
            except:
                print("invalid input")


    elif e=='n':
        print("thank you")
        x=True
    elif e=='l':
        print("team A",team.list1)
        print("team B",team.list2)
        f=open('gfx.txt','a+')
        f.writelines(team.list1 )
        f.writelines((team.list2))
        f.close()
        x=True
        


