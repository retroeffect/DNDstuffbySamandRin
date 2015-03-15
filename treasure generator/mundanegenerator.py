#generates 3.5e dnd mundanes
#function by Rin
import random
def genmundane(int):
    mundanenum = int
    mundanename = 0
    mundanestacks = 0
    mundanevalue = 0
    mundanepercent = 0
    mundanepercenttwo = 0
    mundanepercentthree = 0
    mundanepercent = random.randrange(1,100)
    if mundanepercent <= 17:
        print ("alchemical item")
        if mundanepercenttwo <=12:
            mundanestacks = random.randrange(1,4)
            mundanevalue = 20 * mundanestacks
            print ("you got ",mundanestacks,"flasks of alchemists fire"
            print ("worth",mundanevalue,"gp")
        elif mundanepercenttwo <= 24:
            mundanestacks = random.randrange(2,8)
            mundanevalue = mundanestacks * 10
            print ("you got ",mundanestacks,"flasks of acid")
            print ("worth",mundanevalue,"gp")
        elif mundanepercenttwo <=36:
            mundanestacks = random.randrange(1,4)
            mundanevalue = mundanestacks * 20
            print ("you got ",mundanestacks,"smokesticks")
            print ("worth",mundanevalue,"gp")
        elif mundanepercenttwo <=48:
            mundanestacks = random.randrange(1,4)
            mundanevalue = mundanestacks * 25
            print ("you got ",mundanestacks,"flasks of holy water")
            print ("worth",mundanevalue,"gp")
        elif mundanepercenttwo <=62:
            mundanestacks = random.randrange(1,4)
            mundanevalue = mundanestacks * 50
            print ("you got ",mundanestacks,"doses of antitoxin")
            print ("worth",mundanevalue,"gp")
        elif mundanepercenttwo <=74:
            print ("you got an everburning torch")
        elif mundanepercenttwo <=88:
            mundanestacks = random.randrange(1,4)
            mundanevalue = mundanestacks * 50
            print ("you got ",mundanestacks,"tanglefoot bags")
            print ("worth",mundanevalue,"gp")
        elif mundanepercenttwo <=100:
            mundanestacks = random.randrange(1,4)
            mundanevalue = mundanestacks * 10
            print ("you got ",mundanestacks,"thunderstones")
            print ("worth",mundanevalue,"gp")
    elif mundanepercent <= 50:
        print ("armor")
        mundanepercenttwo = random.randrange(1,100)
        if mundanepercenttwo <= 10:
            print ("small")
        else:
            print ("medium")
        mundanepercenttwo = random.randrange(1,100)
        if mundanepercenttwo <= 12:
            print ("chain shirt")
            print ("worth 100gp")
        elif mundanepercenttwo <= 18:
            print ("masterwork studded leather")
            print ("worth 175gp")
        elif mundanepercenttwo <= 26:
            print ("breastplate")
            print ("worth 200gp")
        elif mundanepercenttwo <= 34:
            print ("Banded mail")
            print ("worth 250gp")
        elif mundanepercenttwo <=54:
            print ("half-plate")
            print ("worth 600gp")
        elif mundanepercenttwo <=80:
            print ("full plate")
            print ("worth 1500gp")
        elif mundanepercenttwo <=90:
            print ("darkwood")
            mundanepercentthree = random.randrange(1,100)
            if mundanepercentthree <= 50:
                print ("buckler")
                print ("worth 205gp")
            else:
                print ("shield")
                print ("worth 257gp")
        elif mundanepercenttwo <= 100:
            print ("masterwork shield")
            mundanepercentthree = random.randrange(1,100)
            if mundanepercentthree <= 17:
                   print ("buckler worth 165gp")
            if mundanepercentthree <= 40:
                   print ("light wooden shield worth 153gp")
            if mundanepercentthree <= 60:
                   print ("light steel shield worth 159gp")
            if mundanepercentthree <= 83:
                   print ("heavy wooden shield worth 157gp")
            if mundanepercentthree <= 100:
                   print ("heavy steel shield worth 170gp")
    elif mundanepercent <= 83:
        print ("weapons")
        mundanepercenttwo = random.randrange(1,100)
        if mundanepercenttwo <= 50:
            print ("masterwork common melee weapon")
        elif mundanepercenttwo <= 70:
            print ("masterwork uncommon weapon")
        elif mundanepercenttwo <=100:
            print ("masterwork common ranged weapon")
    elif mundanepercent <= 100:
        if mundanepercenttwo <= 3:
            print ("empty backpack worth 2gp")
        elif mundanepercenttwo <= 6:
            print ("crowbar worth 2gp")
        elif mundanepercenttwo <= 11:
            print ("bullseye lantern worth 12gp")
        elif mundanepercenttwo <= 16:
            print ("lock, simple worth 20gp")
        elif mundanepercenttwo <= 21:
            print ("lock, average worth 40gp"
        elif mundanepercenttwo <= 28:
            print ("lock, good worth 80gp")
        elif mundanepercenttwo <= 35:
            print ("lock, superior worth 150gp")
        elif mundanepercenttwo <= 40:
            print ("manacles, masterwork worth 50gp")
        elif mundanepercenttwo <= 43:
            print ("mirror,small steel worth 10gp")
        elif mundanepercenttwo <= 46:
            print ("50 ft silk rope worth 10gp")
        elif mundanepercenttwo <= 53:
            print ("spyglass worth 1000gp")
        elif mundanepercenttwo <= 58:
            print ("masterwork artisans tools worth 55gp")
        elif mundanepercenttwo <= 63:
            print ("climbers kit worth 80gp")
        elif mundanepercenttwo <= 68:
            print ("disguise kit worth 50gp")
        elif mundanepercenttwo <= 73:
            print ("healers kit worth 50gp")
        elif mundanepercenttwo <= 77:
            print ("silver holy symbol worth 25gp")
        elif mundanepercenttwo <= 81:
            print ("hourglass worth 25gp")
        elif mundanepercenttwo <= 88:
            print ("magnifying glass 100gp")
        elif mundanepercenttwo <= 95:
            print ("musical instrument, masterwork worth 100gp")
        else:
            print ("thieves tools, masterwork worth 50gp")
