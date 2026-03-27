'''
Problem 1: Calculate Tournament Placement
In the Player class below, each player has a race_outcomes attribute which holds a list of
integers describing what place they came in for each race in a tournament.

Write a method get_tournament_place() that takes in one parameter, opponents, a list of other
player objects also participating in the tournament, and returns the place in the overall
tournament.

Rank in the tournament is determined by the lowest average race outcome. (1st place is better
than 2nd!)
Each opponent in opponents is guaranteed to have participated in the same number of races as
the current player.
'''

class Player:
	def __init__(self, character, kart, outcomes):
		self.character = character
		self.kart = kart
		self.items = []
		self.race_outcomes = outcomes

	def get_tournament_place(self, opponents):
		pass

player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents = [player2, player3]
print(player1.get_tournament_place(opponents)) # 1

'''
Problem 2: Update Linked List Sequence
A linked list is a data structure that allows us to store pieces of data sequentially, similar
to a normal list or array. The key difference between a linked list and a normal list is how
each element is stored in a computer's memory.

In a normal list, individual elements are stored in adjacent memory locations according to
their order in the list. If we know where the first element is stored, it's easy to access any
other element in the list.

In a linked list, individual elements, called nodes, are not stored in sequential memory
locations. Each node may be stored in an unrelated memory location. To connect nodes into a
sequential list, each node stores a reference or pointer to the next node in the list.

Using the provided Node class and the linked list below, update the current linked list
shy_guy -> diddy_kong -> dry_bones to
shy_guy -> link -> diddy_kong -> toad -> dry_bones.

A function print_linked_list() that accepts the head, or first element, of a linked list and
prints the values of the list has also been provided for testing purposes.
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def print_linked_list(head):
	current = head
	while current:
		print(current.value, end=" -> " if current.next else "\n")
		current = current.next

shy_guy = Node("Shy Guy")
diddy_kong = Node("Diddy Kong")
dry_bones = Node("Dry Bones")
shy_guy.next = diddy_kong
diddy_kong.next = dry_bones

link = Node("Link")
toad = Node("Toad")
shy_guy.next = link
link.next = diddy_kong
diddy_kong.next = toad
toad.next = dry_bones

print("Current List:")
print_linked_list(shy_guy)
# Current List:
# Shy Guy -> Link -> Diddy Kong -> Toad -> Dry Bones

'''
Problem 3: Insert Node as Second Element
Write a function add_second() that takes in the head of a linked list and a value val as
parameters. It should insert val as the second node in the linked list and return the head of
the linked list. (You can assume head is not None.)

Note: The "head" of a linked list is the first element in the linked list. It is equivalent to
lst[0] of a normal list.
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def print_linked_list(head):
	current = head
	while current:
		print(current.value, end=" -> " if current.next else "\n")
		current = current.next

def add_second(head, val):
	pass

original_list_head = Node("banana")
second = Node("blue shell")
third = Node("bullet bill")
original_list_head.next = second
second.next = third

new_list = add_second(original_list_head, "red shell")
print_linked_list(new_list) # banana -> red shell -> blue shell -> bullet bill

'''
Problem 4: Increment Linked List Node Values
Write a function increment_ll() that takes in the head of a linked list of integer values and
returns the same list, but with each node's value incremented by 1. Return the head of the
list.
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def print_linked_list(head):
	current = head
	while current:
		print(current.value, end=" -> " if current.next else "\n")
		current = current.next

def increment_ll(head):
	pass

node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

print_linked_list(increment_ll(node_one)) # 6 -> 7 -> 8

'''
Problem 5: Copy Linked List
Write a function copy_ll() that takes in the head of a linked list and creates a complete copy
of that linked list.

The function should return the head of a new linked list which is identical to the given list
in terms of its structure and contents, but does not use any of the node objects from the
original list.
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def print_linked_list(head):
	current = head
	while current:
		print(current.value, end=" -> " if current.next else "\n")
		current = current.next

def copy_ll(head):
	pass

mario = Node("Mario")
daisy = Node("Daisy")
luigi = Node("Luigi")
mario.next = daisy
daisy.next = luigi

copy = copy_ll(mario)
mario.value = "Original Mario"

print_linked_list(mario) # Original Mario -> Daisy -> Luigi
print_linked_list(copy) # Mario -> Daisy -> Luigi

'''
Problem 6: Making the Cut
Imagine that a linked list is used to track the order players finished in a race. Write a
function top_n_finishers() that takes in the head of a linked list and a non-negative integer
n as parameters.

The function should return a list of the values of the first n nodes.

If n is greater than the length of the linked list, return a list of the values of all nodes
in the linked list.
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def print_linked_list(head):
	current = head
	while current:
		print(current.value, end=" -> " if current.next else "\n")
		current = current.next

def top_n_finishers(head, n):
	pass

head = Node("Daisy", Node("Mario", Node("Toad", Node("Yoshi"))))

print(top_n_finishers(head, 3)) # ["Daisy", "Mario", "Toad"]
print(top_n_finishers(head, 5)) # ["Daisy", "Mario", "Toad", "Yoshi"]

'''
Problem 7: Remove Racer
Write a function remove_racer() that takes in the head of a linked list and a value racer as
parameters.

The function should remove the first node with the value racer from the linked list and return
the head of the modified list. If racer is not in the list, return the head of the original
list.
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def print_linked_list(head):
	current = head
	while current:
		print(current.value, end=" -> " if current.next else "\n")
		current = current.next

def remove_racer(head, racer):
	pass

head = Node("Daisy", Node("Mario", Node("Toad", Node("Mario"))))

print_linked_list(remove_racer(head, "Mario")) # Daisy -> Mario -> Toad
print_linked_list(remove_racer(head, "Yoshi")) # Daisy -> Mario -> Toad

'''
Problem 8: Array to Linked List
Write a function arr_to_ll() that accepts an array of Player instances arr and converts arr
into a linked list. The function should return the head of the linked list. If arr is empty,
return None.

A function print_linked_list() which accepts the head, or first element, of a linked list and
prints the character attribute of each Player in the linked list has also been provided for
testing purposes.
'''

class Player:
	def __init__(self, character, kart):
		self.character = character
		self.kart = kart
		self.items = []

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def print_linked_list(head):
	current = head
	while current:
		print(current.value.character, end=" -> " if current.next else "\n")
		current = current.next

def arr_to_ll(arr):
	pass

mario = Player("Mario", "Mushmellow")
luigi = Player("Luigi", "Standard LG")
peach = Player("Peach", "Bumble V")

print_linked_list(arr_to_ll([mario, luigi, peach])) # Mario -> Luigi -> Peach
print_linked_list(arr_to_ll([peach])) # Peach

'''
Problem 9: Convert Singly Linked List to Doubly Linked List
One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node
only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly
linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Update the code below to convert the singly linked list to a doubly linked list.

Two functions, print_linked_list() and print_linked_list_backwards(), have been provided for
testing purposes. print_linked_list() accepts the head of a linked list and prints the values
of each node in the list, starting at the head and iterating in a forward direction.
print_linked_list_backwards() accepts the tail of a linked list and prints the values of each
node in the list, starting at the tail and iterating in a backward direction.
'''

class Node:
	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev

def print_linked_list(head):
	curr = head
	vals = []
	while curr:
		vals.append(str(curr.value))
		curr = curr.next
	print(" -> ".join(vals))

def print_linked_list_backwards(tail):
	curr = tail
	vals = []
	while curr:
		vals.append(str(curr.value))
		curr = curr.prev
	print(" -> ".join(vals))

koopa_troopa = Node("Koopa Troopa")
toadette = Node("Toadette")
waluigi = Node("Waluigi")
koopa_troopa.next = toadette
toadette.next = waluigi

toadette.prev = koopa_troopa
waluigi.prev = toadette

print_linked_list(koopa_troopa) # Koopa Troopa -> Toadette -> Waluigi
print_linked_list_backwards(waluigi) # Waluigi -> Toadette -> Koopa Troopa

'''
Problem 10: Find Length of Doubly Linked List from Any Node
Write a function get_length() that takes in a node at an unknown position within a doubly
linked list. The function should return the length of the entire list.
'''

class Node:
	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev

def print_linked_list(head):
	current = head
	while current:
		print(current.value, end=" -> " if current.next else "\n")
		current = current.next

def get_length(node):
	pass

yoshi_falls = Node("Yoshi Falls")
moo_moo_farm = Node("Moo Moo Farm")
rainbow_road = Node("Rainbow Road")
dk_mountain = Node("DK Mountain")
yoshi_falls.next = moo_moo_farm
moo_moo_farm.next = rainbow_road
rainbow_road.next = dk_mountain
dk_mountain.prev = rainbow_road
rainbow_road.prev = moo_moo_farm
moo_moo_farm.prev = yoshi_falls

print(get_length(rainbow_road)) # 4
