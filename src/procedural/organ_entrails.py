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

supplies = ["Duct Tape", "Paracord", "Pack of Gum", "Garden Hose", "Half Empty Can of Axe Body Spray", "Petunia"]

inventory = {"Toilet Paper": 5,
             "Duct Tape": 1,
             "Paracord": 1,
             "Pack of Gum": 1,
             "Garden Hose": 0,
             "Half Empty Can of Axe Body Spray": 0,
             "Petunia": 0
             }

myWeapons = ["Crowbar"]

runAway = False

print (welcome)
print ("\nLook, a small horde of zombies approaches! Take this crowbar and go bash some heads!")

ready = raw_input("Ready to fight?\n")

if (str.upper(ready) != "Y"):
    print "Too bad, this is Zombietown. You better get ready."
else:
    print "Lock and load!"

zombies = 3
print(str(zombies) + " zombies approach. Ready your " + str.lower(myWeapons[0]) + "!")


attack = raw_input("Attack, or Run? (A for attack, R for run)\n")

if (str.upper(attack) != "A"):
    hit = zombies * hitMultiplier[random.randrange(0, len(hitMultiplier))]
    print(str(hit))
    life = life - hit
    if (hit == 0):
        print("That was a lucky miss. Next time you should attack!")
    else:
        print(str(zombies) + "zombies ravaged you. Your life health is now" + str(life))
else:
    hit = zombies-1 * (hitMultiplier[random.randrange(0, len(hitMultiplier)-4)])
    life = life - hit
    print (str(zombies) + " attack you.\n" "Life health is now " + str(life))
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

print("Now let's go loot a house")
loot = raw_input("Loot house? (Y/N)\n")
if(str.upper(loot) == "Y"):
    foundItem = foundItem = supplies[random.randrange(0, len(supplies)-1)]
    foundWeapon = weapon.keys()[random.randrange(1, len(weapon)-1)]
    zombies = random.randrange(0, 4)
    print(str(zombies) + " zombies found in house.")
    if zombies != 0:
        attack = raw_input("Attack or Run? (A/R)")
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

