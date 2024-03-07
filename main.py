import random

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} added to your inventory.")

def river(player):
    print("You come to a river.")
    choice = input("You can walk around it or swim across. Type 'walk' or 'swim': ").lower()
    if choice == "swim":
        print("You bravely swim across the river...")
        if random.random() < 0.5:
            print("...and successfully reach the other side!")
            bridge_encounter(player)
        else:
            print("...but you encounter an alligator and unfortunately get eaten.")
    elif choice == "walk":
        print("You choose to walk around the river.")
        print("After a long journey, you continue on your path.")
        bridge_encounter(player)
    else:
        print("Invalid choice. Try again.")
        river(player)

def bridge_encounter(player):
    print("You come to a bridge.")
    choice = input("It looks wobbly. Do you want to cross it or head back? Type 'cross' or 'back': ").lower()
    if choice == "cross":
        print("You cautiously cross the bridge...")
        if random.random() < 0.7:
            print("...and successfully reach the other side!")
            stranger_encounter(player)
        else:
            print("...but the bridge collapses under your weight and you fall into the river below.")
            river(player)
    elif choice == "back":
        print("You decide to head back.")
        print("As you turn back, you hear noises behind you...")
        print("A thief emerges from the shadows and attacks you!")
        print("You fight back but unfortunately, the thief overpowers you and steals all your belongings.")
    else:
        print("Invalid choice. Try again.")
        bridge_encounter(player)

def stranger_encounter(player):
    print("As you cross the bridge, you encounter a stranger.")
    choice = input("Do you want to talk to them? Type 'yes' or 'no': ").lower()
    if choice == "yes":
        print("You strike up a conversation with the stranger.")
        print("They turn out to be a friendly traveler and offer you a bag full of gold coins!")
        player.add_to_inventory("gold coins")
        print("Congratulations, you're now rich!")
    elif choice == "no":
        print("You ignore the stranger and continue on your journey.")
        print("However, the stranger seems offended and suddenly attacks you!")
        print("You defend yourself but unfortunately, you're not able to escape unscathed.")
    else:
        print("Invalid choice. Try again.")
        stranger_encounter(player)

def start_adventure():
    name = input("Type your name: ")
    player = Player(name)
    print("Welcome, ", name, ", to this adventure!")

    print("You find yourself on a dirt road. It has come to an end and you can go left or right.")
    direction = input("Which way do you want to go? Type 'left' or 'right': ").lower()

    if direction == "left":
        river(player)
    elif direction == "right":
        bridge_encounter(player)
    else:
        print("Not a valid direction. A bear appears and attacks you!")
        print("You struggle to defend yourself but unfortunately, the bear overwhelms you.")
        print("Game over.")

    print("Thank you for trying, ", name, ". Your inventory:", player.inventory)

start_adventure()
