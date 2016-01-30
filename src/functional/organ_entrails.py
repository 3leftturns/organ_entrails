#!/usr/bin python

import random

__author__ = 'andrewjohnson'


#Zombie game similar to Oregon Trail
#CC 2015 Non-Commercial use Attribution license

welcome = "Welcome to Organ Entrails!\nYou must make it from city to city, killing zombies along the way.\nCareful, they bite!"

life = 20

zombies = 0

hitMultiplier = [0, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4]

weapon = {"Crowbar": 1, "Pistol": 2, "Shovel": 3, "Crossbow": 4, "Shotgun": 5, "Bazooka": 7}

supplies = ["Duct Tape", "Paracord", "Pack of Gum", "Garden Hose", "Half Empty Can of Axe Body Spray", "Petunia", "Candy Bar"]

inventory = {"Toilet Paper": 5,
             "Duct Tape": 1,
             "Paracord": 1,
             "Pack of Gum": 1,
             "Garden Hose": 0,
             "Half Empty Can of Axe Body Spray": 0,
             "Petunia": 0,
             "Candy Bar" : 0
             }

flavorText = {"Toilet Paper": "The soft cottonelle does wonders for your chapped skin. It's the little things to be thankful for.",
              "Duct Tape": "Pretty much good for everything-- wrap a steak in it and it will keep indefinitely.",
              "Paracord": "Your braided bracelet makes you look cool and if you get lost you'll have like 7 feet of rope.",
              "Pack of Gum": "The flavor only lasts for a moment. Alas, this is cheap gum, and the good stuff is hard to come by.",
              "Garden Hose": "Hooking up the hose to the spigot provides adequate water for your beautiful petunias.",
              "Half Empty Can of Axe Body Spray": "The awkward smell of middle school envelopes your body, reminding you of the futility of life.",
              "Petunia": "It never hurts to make an Apocalypse beautiful.",
              "Candy Bar" : "Slightly sweet, slightly sour with rich tones of military surplus rations. Still, it ain't bad."
            }

myWeapons = ["Crowbar"]

cities = ["Zombietown", "The Wastelands", "Detroit", "Brainsville"]
youAreHere = 0

def fightZombies(zombies):
    global life
    print(str(zombies) + " zombies stagger towards you. Ready your " + str.lower(myWeapons[0]) + "!\n")
    attack = raw_input("Attack, or Run? (A for attack, R for run)\n")
    if (str.upper(attack) != "A"):
        hit = (hitMultiplier[random.randrange(0, len(hitMultiplier))]*weapon[myWeapons[0]]) - zombies
        print(str(hit))
        if hit > 0:
            life = life - hit
        if (hit == 0):
            print("That was a lucky miss. Next time you should attack!")
        else:
            print(str(zombies) + " zombies ravaged you. Your life health is now " + str(life))
    else:
        hit = (hitMultiplier[random.randrange(0, len(hitMultiplier))]*weapon[myWeapons[0]]) - zombies
        if hit > 0:
            life = life - hit
        print (str(zombies) + " attack you.\n" "Life health is now " + str(life))


def lootHouse():
    global life
    runAway = False
    loot = raw_input("Loot house? (Y/N)\n")
    if(str.upper(loot) == "Y"):
        foundItem = supplies[random.randrange(0, len(supplies)-1)]
        foundWeapon = weapon.keys()[random.randrange(1, len(weapon)-1)]
        zombies = random.randrange(0, 4)
        print(str(zombies) + " zombies found in house.")
        if zombies != 0:
            attack = raw_input("Attack or Run? (A/R)\n")
            if str.upper(attack) == "A":
                hit = zombies-1 * (hitMultiplier[random.randrange(0, len(hitMultiplier)-4)])
                life = life - hit
                print (str(zombies) + " attack you.\n" "Life health is now " + str(life))
            else:
                runAway = True
                print("You run away quietly, with no cool stuff.")
        else:
            print ("The house is empty of zombies, but full of cool stuff...")
        if (runAway != True):
            takeItem = raw_input("You found a " + foundItem + "\nEquip? (Y/N)")
            takeWeapon = raw_input("Cool! You found a " + foundWeapon + "\nEquip? (Y/N)")
            if str.upper(takeWeapon) == "Y": myWeapons.insert(0, foundWeapon)
            if str.upper(takeItem) == "Y": inventory[foundItem] += 1
            print ("Current weapon: " + str(myWeapons[0]))
            print ("Destruction power: " + str(weapon[myWeapons[0]]))
            print("Inventory:\n==========")
            for item in inventory:
                if(inventory[item] > 0):
                    print (item + ": " + str(inventory[item]))
            print("\n")

def lootBodies():
    loot = raw_input("Would you like to loot the bodies? (Y/N)\n")
    if (str.upper(loot) == "Y"):
        if (random.randrange(0,9)>8):
            print("A zombie was not yet dead!\n")
            hit = 1 * hitMultiplier[random.randrange(0, len(hitMultiplier))]
            life = life - hit
            print("Zombie did " + str(hit) + " damage to you.\nYour life is " + str(life))
        else:
            foundItem = supplies[random.randrange(0, len(supplies)-1)]
            print("You found a " + foundItem)
            equip = raw_input("Equip? (Y/N)")
            if (str.upper(equip) == "Y"):
                inventory[foundItem] += 1
                print ("Inventory: " + str(inventory))

def leaveCity():
    global cities
    global youAreHere
    print("Where would you like to go? You are currently in " + cities[youAreHere])
    whereTo = ""
    i = 1
    for city in cities:
        if city != cities[youAreHere]:
            whereTo = whereTo + "   " + str(i) + ") " + city + "\n"
            i = i + 1
    cityIndex =  int(raw_input("I want to go to: " + "\n" + whereTo))
    youAreHere = cityIndex
    print("Welcome to " + cities[youAreHere])

def checkInventory():
    global life
    global flavorText
    print ("Current weapon: " + str(myWeapons[0]))
    print ("Destruction power: " + str(weapon[myWeapons[0]]))
    print("Inventory:\n==========")
    i = 1
    invArray = []
    for item in inventory:
        if(inventory[item] > 0):
            print (str(i) + ") " + item + ": " + str(inventory[item]))
            invArray.append(item)
            i = i + 1
    print str(i) + ") Exit Inventory"
    inventoryIndex = int(raw_input("Select the item from the list.\n"))-1
    if inventoryIndex != len(invArray):
        myItem = invArray[inventoryIndex]
        if myItem == "Candy Bar":
            life = life + 5
        print flavorText[myItem]
        inventory[myItem] -= 1


def changeWeapon():
    print("Current weapon equipped: " + myWeapons[0])
    print ("Select weapon to equip from the list.")
    i = 1
    for weapon in myWeapons:
        print str(i) + ") " + weapon
        i += 1
    equip = int(raw_input("Equip:\n"))-1
    w = myWeapons.pop(equip)
    myWeapons.insert(0, w)

    print myWeapons[0] + " is equipped.\n"


print (welcome)
print ("\nLook, a small horde of zombies approaches! Take this crowbar and go bash some heads!")

ready = raw_input("Ready to fight?\n")

if (str.upper(ready) != "Y"):
    print "Too bad, this is Zombietown. You better get ready.\n"
else:
    print "Lock and load!\n"

fightZombies(3)
lootBodies()

print("Now let's go loot a house")
lootHouse()

print("You seem to be getting this on your own. Here's a candy bar to restore your health, and one for the road. \n")
inventory["Candy Bar"] += 1
life = 20

while (life > 0):
    print("Life: " + str(life))
    action = raw_input("What would you like to do now?\n1)Find more zombies\n2)Loot more houses\n3)Leave the city\n4)Check inventory\n5)Change Weapon\n\n")
    if (action == "1"):
        fightZombies(random.randrange(0, 10))
        if (life > 0):
            lootBodies()
    elif (action == "2"):
        lootHouse()
    elif (action == "3"):
        leaveCity()
    elif (action == "4"):
        checkInventory()
    elif (action == "5"):
        changeWeapon()
    else:
        print("Invalid input!")

print("You died.")
