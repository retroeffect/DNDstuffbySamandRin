# think of importing things like file drawers. A computer has tons of file drawers because it knows many things. However, it doesn't know much of anything until you
#tell it to open the drawer. When you import something, you tell the computer to open a specific drawer. Here, we told it to open the "we're going to ask you for
#random numbers" drawer.
import random
print ("Welcome to the improved 3.5 treasure generator.")
# this tells the computer what each variable means. When you code, you have to think like a computer.
# this is a trick programers use. It's telling the computer that as long as 1= 1 (which is forever) to continue doing whatever we say next.
#the majority of this code is written by Sam

#dnd art object generator function
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

def gemgenerator(int):
    numofgems = int
    while numofgems >= 1:
        gemvalue = 0
        percentiledie = random.randrange(1,100)
        print (percentiledie, "%d")
        if percentiledie <= 25:
            gemvalue = random.randrange(4,16)
            print ("gem value",gemvalue, "gp")
            print ("examples: Banded, eye, or moss agate; azurite; blue quartz; hematite; lapis lazuli; malachite; obsidian; rhodochrosite; tiger eye turquoise; freshwater (irregular) pearl")
            print ("")
        elif percentiledie <= 50:
            gemvalue = random.randrange(4,16)
            print ("gem value",gemvalue, "gp")
            print ("examples:Bloodstone; carnelian; chalcedony; chrysoprase; citrine; iolite, jasper; moonstone; onyx; peridot; rock crystal (clear quartz); sard; sardonyx; rose, smoky, or star rose quartz; zircon")
            print ("")
        elif percentiledie <= 70:
            gemvalue = random.randrange(2,8) * 10
            print ("gem value",gemvalue, "gp")
            print ("examples:Amber; amethyst; chrysoberyl; coral; red or brown-green garnet; jade; jet; white, golden, pink, or silver pearl; red spinel, red-brown or deep green spinel; tourmaline")
        elif percentiledie <= 90:
            gemvalue = random.randrange(4,16) * 10
            print ("gem value",gemvalue, "gp")
            print ("examples:Alexandrite; aquamarine; violet garnet; black pearl; deep blue spinel; golden yellow topaz")
            print ("")
        elif percentiledie <= 99:
            gemvalue = random.randrange(2,8) * 100
            print ("gem value",gemvalue, "gp")
            print ("examples:Emerald; white, black, or fire opal; blue sapphire; fiery yellow or rich purple corundum; blue or black star sapphire; star ruby")
            print ("")
        elif percentiledie == 100:
            gemvalue = random.randrange(2,8) * 1000
            print ("gem value",gemvalue, "gp")
            print ("Clearest bright green emerald; blue-white, canary, pink, brown, or blue diamond; jacinth")
            print ("")
        numofgems = numofgems - 1



# think of importing things like file drawers. A computer has tons of file drawers because it knows many things. However, it doesn't know much of anything until you
#tell it to open the drawer. When you import something, you tell the computer to open a specific drawer. Here, we told it to open the "we're going to ask you for
#random numbers" drawer.
#I think I ended on number 10 ish, however I copied and pasted for each. Reading will be weird. Sorry bout that :(
import random
print ("Welcome to the improved 3.5 treasure generator.")
# this tells the computer what each variable means. When you code, you have to think like a computer.
# this is a trick programers use. It's telling the computer that as long as 1= 1 (which is forever) to continue doing whatever we say next.
while 1==1:
   coins = random.randint(1,100)
   goods = random.randint(1,100)
   items = random.randint(1,100)
   coinsearned = 0
   goodsearned = 0
   itemsearned = 0
   level = input()
   if level == '1':
        print ("coins", coins, "goods", goods, "items", items)
#this block determines the amount and type of coins
        if coins <= 14:
            print ("no coins")
        elif coins <= 29:
#1d6 * 1000 cp
            coinsearned = random.randrange(1,6) * 1000
            print (coinsearned,"cp") 
        elif coins <= 52:
#1d8 * 100 sp
            coinsearned = random.randrange(1,8) * 100
            print (coinsearned,"sp")
        elif coins <= 95:
#2d8 * 10 gp
            coinsearned = random.randrange(2,16) * 10
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(1,4) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 90:
            print ("no goods")
        elif goods <= 95:
#91 < %d > 96 = 1 gem
            goodsearned = 1
            print (goodsearned,"gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = 1
            print (goodsearned,"art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 71:
#0 < %d > 72
            print ("no items")
        elif items <= 95:
#71 < %d > 95
            itemsearned = "1 mundane"
            print (itemsearned)
        elif items <= 100:
#95 < %d
            itemsearned = "1 minor"
            print (itemsearned)



   elif level == '2':
        print ("coins", coins, "goods", goods, "items", items)
        #this block determines the amount and type of coins
        if coins <= 13:
            print ("no coins")
        elif coins <= 23:
#1d6 * 1000 cp
            coinsearned = random.randrange(1,10) * 1000
            print (coinsearned,"cp") 
        elif coins <= 43:
#1d8 * 100 sp
            coinsearned = random.randrange(2,20) * 100
            print (coinsearned,"sp")
        elif coins <= 95:
#2d8 * 10 gp
            coinsearned = random.randrange(4,40) * 10
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(2,8) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 81:
            print ("no goods")
        elif goods <= 95:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,3)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,3)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 49:
#0 < %d > 72
            print ("no items")
        elif items <= 85:
#71 < %d > 95
            itemsearned = "1 mundane"
            print (itemsearned)
        elif items <= 100:
#95 < %d
            itemsearned = "1 minor"
            print (itemsearned)
        


   elif level == '3':
        print ("coins", coins, "goods", goods, "items", items)
        #this block determines the amount and type of coins
        if coins <= 11:
            print ("no coins")
        elif coins <= 21:
#1d6 * 1000 cp
            coinsearned = random.randrange(2,20) * 1000
            print (coinsearned,"cp") 
        elif coins <= 41:
#1d8 * 100 sp
            coinsearned = random.randrange(4,32) * 100
            print (coinsearned,"sp")
        elif coins <= 95:
#2d8 * 10 gp
            coinsearned = random.randrange(1,4) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(1,10) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 77:
            print ("no goods")
        elif goods <= 95:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,3)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,3)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 49:
#0 < %d > 72
            print ("no items")
        elif items <= 79:
#71 < %d > 95
            itemsearned = random.randrange(1,3)
            print (itemsearned, "mundane")
        elif items <= 100:
#95 < %d
            itemsearned = "1 minor"
            print (itemsearned)
        


   elif level == '4':
        print ("coins", coins, "goods", goods, "items", items)
        #this block determines the amount and type of coins
        if coins <= 11:
            print ("no coins")
        elif coins <= 21:
#1d6 * 1000 cp
            coinsearned = random.randrange(3,30) * 1000
            print (coinsearned,"cp") 
        elif coins <= 41:
#1d8 * 100 sp
            coinsearned = random.randrange(4,48) * 1000
            print (coinsearned,"sp")
        elif coins <= 95:
#2d8 * 10 gp
            coinsearned = random.randrange(1,6) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(1,8) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 70:
            print ("no goods")
        elif goods <= 95:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,4)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,3)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 42:
#0 < %d > 72
            print ("no items")
        elif items <= 62:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "mundane")
        elif items <= 100:
#95 < %d
            itemsearned = "1 minor"
            print (itemsearned)



   elif level == '5':
        print ("coins", coins, "goods", goods, "items", items)
                #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 19:
#1d6 * 1000 cp
            coinsearned = random.randrange(1,4) * 10000
            print (coinsearned,"cp") 
        elif coins <= 38:
#1d8 * 100 sp
            coinsearned = random.randrange(1,6) * 1000
            print (coinsearned,"sp")
        elif coins <= 95:
#2d8 * 10 gp
            coinsearned = random.randrange(1,8) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(1,10) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 60:
            print ("no goods")
        elif goods <= 95:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,4)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 57:
#0 < %d > 72
            print ("no items")
        elif items <= 67:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "mundane")
        elif items <= 100:
#95 < %d
            itemsearned = random.randrange(1,3)
            print (itemsearned, "minor")



   elif level == '6':
        print ("coins", coins, "goods", goods, "items", items)
        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 18:
#1d6 * 1000 cp
            coinsearned = random.randrange(1,6) * 10000
            print (coinsearned,"cp") 
        elif coins <= 37:
#1d8 * 100 sp
            coinsearned = random.randrange(1,8) * 1000
            print (coinsearned,"sp")
        elif coins <= 95:
#2d8 * 10 gp
            coinsearned = random.randrange(1,10) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(1,12) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 56:
            print ("no goods")
        elif goods <= 92:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,4)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 54:
#0 < %d > 72
            print ("no items")
        elif items <= 59:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "mundane")
        elif items <= 99:
#95 < %d
            itemsearned = random.randrange(1,3)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)



   elif level == '7':
        print ("coins", coins, "goods", goods, "items", items)
                #this block determines the amount and type of coins
        if coins <= 11:
            print ("no coins")
        elif coins <= 18:
#1d6 * 1000 cp
            coinsearned = random.randrange(1,10) * 10000
            print (coinsearned,"cp") 
        elif coins <= 35:
#1d8 * 100 sp
            coinsearned = random.randrange(1,12) * 1000
            print (coinsearned,"sp")
        elif coins <= 93:
#2d8 * 10 gp
            coinsearned = random.randrange(2,12) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(3,12) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 48:
            print ("no goods")
        elif goods <= 88:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,4)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 51:
#0 < %d > 72
            print ("no items")
        elif items <= 97:
#71 < %d > 95
            itemsearned = random.randrange(1,3)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)


   elif level == '8':
        print ("coins", coins, "goods", goods, "items", items)
                        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 15:
#1d6 * 1000 cp
            coinsearned = random.randrange(1,12) * 10000
            print (coinsearned,"cp") 
        elif coins <= 29:
#1d8 * 100 sp
            coinsearned = random.randrange(2,12) * 1000
            print (coinsearned,"sp")
        elif coins <= 87:
#2d8 * 10 gp
            coinsearned = random.randrange(2,8) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(3,18) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 45:
            print ("no goods")
        elif goods <= 85:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,6)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 48:
#0 < %d > 72
            print ("no items")
        elif items <= 96:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)


   elif level == '9':
        print ("coins", coins, "goods", goods, "items", items)
                                #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 15:
#1d6 * 1000 cp
            coinsearned = random.randrange(2,12) * 10000
            print (coinsearned,"cp") 
        elif coins <= 29:
#1d8 * 100 sp
            coinsearned = random.randrange(2,16) * 1000
            print (coinsearned,"sp")
        elif coins <= 85:
#2d8 * 10 gp
            coinsearned = random.randrange(5,20) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(2,24) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 40:
            print ("no goods")
        elif goods <= 80:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,8)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 43:
#0 < %d > 72
            print ("no items")
        elif items <= 91:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)



   elif level == '10':
        print ("coins", coins, "goods", goods, "items", items)
                                        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins") 
        elif coins <= 24:
#1d8 * 100 sp
            coinsearned = random.randrange(2,20) * 1000
            print (coinsearned,"sp")
        elif coins <= 79:
#2d8 * 10 gp
            coinsearned = random.randrange(6,24) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(5,30) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 35:
            print ("no goods")
        elif goods <= 79:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,8)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,6)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 40:
#0 < %d > 72
            print ("no items")
        elif items <= 91:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)


   elif level == '11':
        print ("coins", coins, "goods", goods, "items", items)
                                        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 15:
#1d6 * 1000 cp
            coinsearned = random.randrange(2,12) * 10000
            print (coinsearned,"cp") 
        elif coins <= 29:
#1d8 * 100 sp
            coinsearned = random.randrange(2,16) * 1000
            print (coinsearned,"sp")
        elif coins <= 85:
#2d8 * 10 gp
            coinsearned = random.randrange(5,20) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(2,24) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 40:
            print ("no goods")
        elif goods <= 80:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,8)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 43:
#0 < %d > 72
            print ("no items")
        elif items <= 91:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)

   elif level == '12':
        print ("coins", coins, "goods", goods, "items", items)
                                        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 15:
#1d6 * 1000 cp
            coinsearned = random.randrange(2,12) * 10000
            print (coinsearned,"cp") 
        elif coins <= 29:
#1d8 * 100 sp
            coinsearned = random.randrange(2,16) * 1000
            print (coinsearned,"sp")
        elif coins <= 85:
#2d8 * 10 gp
            coinsearned = random.randrange(5,20) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(2,24) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 40:
            print ("no goods")
        elif goods <= 80:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,8)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 43:
#0 < %d > 72
            print ("no items")
        elif items <= 91:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)

   elif level == '13':
        print ("coins", coins, "goods", goods, "items", items)
                                        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 15:
#1d6 * 1000 cp
            coinsearned = random.randrange(2,12) * 10000
            print (coinsearned,"cp") 
        elif coins <= 29:
#1d8 * 100 sp
            coinsearned = random.randrange(2,16) * 1000
            print (coinsearned,"sp")
        elif coins <= 85:
#2d8 * 10 gp
            coinsearned = random.randrange(5,20) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(2,24) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 40:
            print ("no goods")
        elif goods <= 80:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,8)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 43:
#0 < %d > 72
            print ("no items")
        elif items <= 91:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)

   elif level == '14':
        print ("coins", coins, "goods", goods, "items", items)
                                        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 15:
#1d6 * 1000 cp
            coinsearned = random.randrange(2,12) * 10000
            print (coinsearned,"cp") 
        elif coins <= 29:
#1d8 * 100 sp
            coinsearned = random.randrange(2,16) * 1000
            print (coinsearned,"sp")
        elif coins <= 85:
#2d8 * 10 gp
            coinsearned = random.randrange(5,20) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(2,24) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 40:
            print ("no goods")
        elif goods <= 80:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,8)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            artgen(goodsearned)
#this block determines the amount and type of items

        if items <= 43:
#0 < %d > 72
            print ("no items")
        elif items <= 91:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)


   elif level == '15':
        print ("coins", coins, "goods", goods, "items", items)
                                        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 15:
#1d6 * 1000 cp
            coinsearned = random.randrange(2,12) * 10000
            print (coinsearned,"cp") 
        elif coins <= 29:
#1d8 * 100 sp
            coinsearned = random.randrange(2,16) * 1000
            print (coinsearned,"sp")
        elif coins <= 85:
#2d8 * 10 gp
            coinsearned = random.randrange(5,20) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(2,24) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 40:
            print ("no goods")
        elif goods <= 80:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,8)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 43:
#0 < %d > 72
            print ("no items")
        elif items <= 91:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)


   elif level == '16':
        print ("coins", coins, "goods", goods, "items", items)
                                        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 15:
#1d6 * 1000 cp
            coinsearned = random.randrange(2,12) * 10000
            print (coinsearned,"cp") 
        elif coins <= 29:
#1d8 * 100 sp
            coinsearned = random.randrange(2,16) * 1000
            print (coinsearned,"sp")
        elif coins <= 85:
#2d8 * 10 gp
            coinsearned = random.randrange(5,20) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(2,24) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 40:
            print ("no goods")
        elif goods <= 80:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,8)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 43:
#0 < %d > 72
            print ("no items")
        elif items <= 91:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)


   elif level == '17':
        print ("coins", coins, "goods", goods, "items", items)
                                        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 15:
#1d6 * 1000 cp
            coinsearned = random.randrange(2,12) * 10000
            print (coinsearned,"cp") 
        elif coins <= 29:
#1d8 * 100 sp
            coinsearned = random.randrange(2,16) * 1000
            print (coinsearned,"sp")
        elif coins <= 85:
#2d8 * 10 gp
            coinsearned = random.randrange(5,20) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(2,24) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 40:
            print ("no goods")
        elif goods <= 80:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,8)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart (goodsearned)
#this block determines the amount and type of items

        if items <= 43:
#0 < %d > 72
            print ("no items")
        elif items <= 91:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)


   elif level == '18':
        print ("coins", coins, "goods", goods, "items", items)
                                        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 15:
#1d6 * 1000 cp
            coinsearned = random.randrange(2,12) * 10000
            print (coinsearned,"cp") 
        elif coins <= 29:
#1d8 * 100 sp
            coinsearned = random.randrange(2,16) * 1000
            print (coinsearned,"sp")
        elif coins <= 85:
#2d8 * 10 gp
            coinsearned = random.randrange(5,20) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(2,24) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 40:
            print ("no goods")
        elif goods <= 80:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,8)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            artgen(goodsearned)
#this block determines the amount and type of items

        if items <= 43:
#0 < %d > 72
            print ("no items")
        elif items <= 91:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)


   elif level == '19':
        print ("coins", coins, "goods", goods, "items", items)
                                        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 15:
#1d6 * 1000 cp
            coinsearned = random.randrange(2,12) * 10000
            print (coinsearned,"cp") 
        elif coins <= 29:
#1d8 * 100 sp
            coinsearned = random.randrange(2,16) * 1000
            print (coinsearned,"sp")
        elif coins <= 85:
#2d8 * 10 gp
            coinsearned = random.randrange(5,20) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(2,24) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 40:
            print ("no goods")
        elif goods <= 80:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,8)
            print (goodsearned, "gems")
            gemgeneraotor
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart(goodsearned)
            
#this block determines the amount and type of items

        if items <= 43:
#0 < %d > 72
            print ("no items")
        elif items <= 91:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)


   elif level == '20':
        print ("coins", coins, "goods", goods, "items", items)
                                        #this block determines the amount and type of coins
        if coins <= 10:
            print ("no coins")
        elif coins <= 15:
#1d6 * 1000 cp
            coinsearned = random.randrange(2,12) * 10000
            print (coinsearned,"cp") 
        elif coins <= 29:
#1d8 * 100 sp
            coinsearned = random.randrange(2,16) * 1000
            print (coinsearned,"sp")
        elif coins <= 85:
#2d8 * 10 gp
            coinsearned = random.randrange(5,20) * 100
            print (coinsearned,"gp")
        elif coins <= 100:
#1d4 * 10 pp
            coinsearned = random.randrange(2,24) * 10
            print (coinsearned,"pp")

#this block determines the amount and type of goods
        if goods <= 40:
            print ("no goods")
        elif goods <= 80:
#91 < %d > 96 = 1 gem
            goodsearned = random.randrange(1,8)
            print (goodsearned, "gems")
            gemgenerator(goodsearned)
        elif goods <= 100:
#95 < %d > 100
            goodsearned = random.randrange(1,4)
            print (goodsearned, "art")
            genart(goodsearned)
#this block determines the amount and type of items

        if items <= 43:
#0 < %d > 72
            print ("no items")
        elif items <= 91:
#71 < %d > 95
            itemsearned = random.randrange(1,4)
            print (itemsearned, "minor")
        elif items <= 100:
            itemsearned = "1 medium"
            print (itemsearned)

   else:
        print ("Please input a different number")






