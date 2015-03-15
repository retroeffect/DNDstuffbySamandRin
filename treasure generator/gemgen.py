#gem generator function for dnd treasure generator
#this function by rin
def gemgenerator(int):
    import random
    numofgems = int
    while numofgems >= 1:
        gemvalue = 0
        percentiledie = random.randrange(1,100)
        print (percentiledie)
        if percentiledie <= 25:
            gemvalue = random.randrange(4,16)
            print (gemvalue, "gp")
            print ("examples: Banded, eye, or moss agate; azurite; blue quartz; hematite; lapis lazuli; malachite; obsidian; rhodochrosite; tiger eye turquoise; freshwater (irregular) pearl")
        elif percentiledie <= 50:
            gemvalue = random.randrange(4,16)
            print (gemvalue, "gp")
            print ("examples:Bloodstone; carnelian; chalcedony; chrysoprase; citrine; iolite, jasper; moonstone; onyx; peridot; rock crystal (clear quartz); sard; sardonyx; rose, smoky, or star rose quartz; zircon")
        elif percentiledie <= 70:
            gemvalue = random.randrange(2,8) * 10
            print (gemvalue, "gp")
            print ("examples:Amber; amethyst; chrysoberyl; coral; red or brown-green garnet; jade; jet; white, golden, pink, or silver pearl; red spinel, red-brown or deep green spinel; tourmaline")
        elif percentiledie <= 90:
            gemvalue = random.randrange(4,16) * 10
            print (gemvalue, "gp")
            print ("examples:Alexandrite; aquamarine; violet garnet; black pearl; deep blue spinel; golden yellow topaz")
        elif percentiledie <= 99:
            gemvalue = random.randrange(2,8) * 100
            print (gemvalue, "gp")
            print ("examples:Emerald; white, black, or fire opal; blue sapphire; fiery yellow or rich purple corundum; blue or black star sapphire; star ruby")
        elif percentiledie == 100:
            gemvalue = random.randrange(2,8) * 1000
            print (gemvalue, "gp")
            print ("Clearest bright green emerald; blue-white, canary, pink, brown, or blue diamond; jacinth")
        numofgems = numofgems - 1
gemgenerator(2)

