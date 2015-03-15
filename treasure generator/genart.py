#dnd art object generator function
#this function by rin
import random
def genart(int):
    artnumber = int
    artvalue = 0
    artpercentdie = 0
    while artnumber >=1:
        artpercentdie = random.randrange(1,100)
        if artpercentdie <= 10:
            artvalue = random.randrange(1,10) * 10
            print ("art value ",artvalue," gp")
            print ("examples:Silver ewer; carved bone or ivory statuette; finely wrought small gold bracelet")
        elif artpercentdie <= 25:
            artvalue = random.randrange(3,18) * 10
            print ("art value ",artvalue," gp")
            print ("examples:Cloth of gold vestments; black velvet mask with numerous citrines; silver chalice with lapis lazuli gems")
        elif artpercentdie <= 40:
            artvalue = random.randrange(1,6) * 100
            print ("art value ",artvalue," gp")
            print ("examples:Large well-done wool tapestry; brass mug with jade inlays")
        elif artpercentdie <= 50:
            artvalue = random.randrange(1,10) * 100
            print ("art value ",artvalue," gp")
            print ("examples:Silver comb with moonstones; silver-plated steel longsword with jet jewel in hilt")
        elif artpercentdie <= 60:
            artvalue = random.randrange(2,12) * 100
            print ("art value ",artvalue," gp")
            print ("examples:Carved harp of exotic wood with ivory inlay and zircon gems; solid gold idol (10 lb.)")
        elif artpercentdie <= 70:
            artvalue = random.randrange(3,18) * 100
            print ("art value ",artvalue," gp")
            print ("examples:Gold dragon comb with red garnet eye; gold and topaz bottle stopper cork; ceremonial electrum dagger with a star ruby in the pommel")
        elif artpercentdie <= 80:
            artvalue = random.randrange(4,16) * 100
            print ("art value ",artvalue," gp")
            print ("examples:Eyepatch with mock eye of sapphire and moonstone; fire opal pendant on a fine gold chain; old masterpiece painting")
        elif artpercentdie <= 85:
            artvalue = random.randrange(5,30) * 100
            print ("art value ",artvalue," gp")
            print ("examples:Embroidered silk and velvet mantle with numerous moonstones; sapphire pendant on gold chain")
        elif artpercentdie <= 90:
            artvalue = random.randrange(1,4) * 1000
            print ("art value ",artvalue," gp")
            print ("examples:Embroidered and bejeweled glove; jeweled anklet; gold music box")
        elif artpercentdie <= 95:
            artvalue = random.randrange(1,6) * 1000
            print ("art value ",artvalue," gp")
            print ("examples:Golden circlet with four aquamarines; a string of small pink pearls (necklace)")
        elif artpercentdie <= 99:
            artvalue = random.randrange(2,8) * 1000
            print ("art value ",artvalue," gp")
            print ("examples:Jeweled gold crown; jeweled electrum ring")
        elif artpercentdie <= 100:
            print ("art value ",artvalue," gp")
            artvalue = random.randrange(2,12) * 1000
            print ("examples:Gold and ruby ring; gold cup set with emeralds")
        artnumber = artnumber - 1
genart(5)
