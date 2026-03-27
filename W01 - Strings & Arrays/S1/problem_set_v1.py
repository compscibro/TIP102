'''
Problem 1: Hundred Acre Wood
Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!"
'''

def welcome():
	pass

# Welcome to The Hundred Acre Wood!

'''
Problem 2: Greeting
Write a function greeting() that accepts a single parameter, a string name, and 
prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."
'''

def greeting(name):
	pass

greeting("Michael") # Welcome to The Hundred Acre Wood Michael! My name is Christopher Robin.
greeting("Winnie the Pooh") # Welcome to The Hundred Acre Wood Winnie the Pooh! My name is Christopher Robin.

'''
Problem 3: Catchphrase
Write a function print_catchphrase() that accepts a string character as a parameter and 
prints the catchphrase of the given character as outlined in the table below.

Character               Catchphrase
"Pooh"                  "Oh bother!"
"Tigger"                "TTFN: Ta-ta for now!"
"Eeyore"                "Thanks for noticing me."
"Christopher Robin"     "Silly old bear."

If the given character does not match one of the characters included above, print "Sorry! 
I don't know <character>'s catchphrase!"
'''

def print_catchphrase(character):
	pass

character = "Pooh"
print_catchphrase(character) # "Oh bother!"

character = "Piglet"
print_catchphrase(character) # "Sorry! I don't know Piglet's catchphrase!"

'''
Problem 4: Return Item
Implement a function get_item() that accepts a 0-indexed list items and a non-negative 
integer x and returns the element at index x in items. If x is not a valid index of items, return None.
'''

def get_item(items, x):
	pass

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x) # "roo"

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x) # None

'''
Problem 5: Total Honey
Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts a list of 
integers hunny_jars and returns the sum of all elements in the list. Do not use the built-in function sum().
'''

def sum_honey(hunny_jars):
	pass

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars) # 14

hunny_jars = []
sum_honey(hunny_jars) # 0

'''
Problem 6: Double Trouble
Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers 
hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.
'''

def doubled(hunny_jars):
	pass

hunny_jars = [1, 2, 3]
doubled(hunny_jars) # [2, 4, 6]

'''
Problem 7: Poohsticks
Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a 
stream and race them. They time how long it takes each player's stick to float under Poohsticks 
Bridge to score each round.

Write a function count_less_than() to help Pooh and his friends determine how many players 
should move on to the next round of Poohsticks. count_less_than() should accept a list of 
integers race_times and an integer threshold and return the number of race times less than threshold.
'''

def count_less_than(race_times, threshold):
	pass

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold) # 3

race_times = []
threshold = 4
count_less_than(race_times, threshold) # 0

'''
Problem 8: Pooh's To Do's
Write a function print_todo_list() that accepts a list of strings named tasks. The function should then number and print each task on a new line using the format:

Pooh's To Dos:
1. Task 1
2. Task 2
...
'''

def print_todo_list(task):
	pass

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)
# Pooh's To Dos:
# 1. Count all the bees in the hive
# 2. Chase all the clouds from the sky
# 3. Think
# 4. Stoutness Exercises

task = []
print_todo_list(task)
# Pooh's To Dos:

'''
Problem 9: Pairs
Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. 
Write a function can_pair() that accepts a list of integers item_quantities. Return True if each 
number in item_quantities is even. Return False otherwise.
'''

def can_pair(item_quantities):
	pass

item_quantities = [2, 4, 6, 8]
can_pair(item_quantities) # True

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities) # False

item_quantities = []
can_pair(item_quantities) # True

'''
Problem 10: Split Haycorns
Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly 
amongst his friends. Write a function split_haycorns() to help Piglet determine the number of 
ways he can split his haycorns into even groups. split_haycorns() accepts a positive integer 
quantity as a parameter and returns a list of all divisors of quantity.
'''

def split_haycorns(quantity):
	pass

quantity = 6
split_haycorns(quantity) # [1, 2, 3, 6]

quantity = 1
split_haycorns(quantity) # [1]

'''
Problem 11: T-I-Double Guh-ER
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any
letters he needs to spell out his name. Write a function tiggerfy() that accepts a string s,
and returns a new string with the letters t, i, g, e, and r removed from it.
'''

def tiggerfy(s):
	pass

s = "suspicerous"
tiggerfy(s) # "suspcous"

s = "Trigger"
tiggerfy(s) # ""

s = "Hunny"
tiggerfy(s) # "Hunny"

'''
Problem 12: Thistle Hunt
Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. 
Write a function locate_thistles() that takes in a list of strings items 
and returns a list of the indices of any elements with value "thistle". 
The indices in the resulting list should be ordered from least to greatest.
'''

def locate_thistles(items):
	pass

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items) # [0, 3]

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items) # []
