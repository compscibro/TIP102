"""class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

# Instantiate your villager here
apollo = Villager("Apollo", "Eagle", "pah")

# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 
"""

# -----

# class Player():
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items = []
        
#     def add_item(self, item_name):

#         special_items = ["banana", "green shell", 
#         "red shell", "bob-omb", "super star", 
#         "lightning", "bullet bill"]

#         if item_name in special_items:
#             self.items.append(item_name)
        
        

# player_one = Player("Yoshi", "Dolphin Dasher")

# print(player_one.items)

# player_one.add_item("red shell")
# print(player_one.items)

# player_one.add_item("super star")
# print(player_one.items)

# player_one.add_item("super smash")
# print(player_one.items)


# plan: 
#   dictionary
#   loop through players items
#   if no items, print "inventory empty"
#   print the name and qty of each item in a player's list
'''
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
    
    def print_inventory(self):
        if(not self.items):
            print("Inventory empty")
        else:
            Inventory = {}
            for item in self.items:
                Inventory[item] = Inventory.get(item, 0) + 1
            #for key, value in Inventory.items():
            result = ", ".join(f"{key}: {value}" for key, value in Inventory.items())
            print("Inventory: " + result) 

player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

player_one.print_inventory()
player_two.print_inventory()
'''

#plan
#loop through race results
#use place variable to keep track of the players place
#print players name and place
'''
class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
    #... methods from previous problems

def print_results(race_results):
    for i,plr in enumerate(race_results):
        print(str(i+1) + ": " + plr.character)



peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)
'''

class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent
        
def get_rank(my_player):
    pass

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

print(get_rank(luigi))
print(get_rank(peach))
print(get_rank(mario))