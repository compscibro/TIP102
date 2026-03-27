'''
Problem 1: Why is it Always You Three
In a single assignment statement, create the linked list Harry -> Ron -> Hermione.
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

head = Node("Harry", Node("Ron", Node("Hermione")))

print_linked_list(head) # Harry -> Ron -> Hermione

'''
Problem 2: 200 Points for Gryffindor
It's almost the end of the year, and Gryffindor students want to see if they have any
competition for first place. Given the head of a linked list house_points and the
Gryffindor's score, return the frequency of score in the list.

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.
'''

class Node:
	def __init__(self, house, score, next=None):
		self.house = house
		self.value = score
		self.next = next

def print_linked_list(head):
	current = head
	while current:
		print((current.house, current.value), end=" -> " if current.next else "\n")
		current = current.next

def count_element(house_points, score):
	pass

house_points = Node("Gryffindor", 600,
				Node("Ravenclaw", 300,
					Node("Slytherin", 500,
						Node("Hufflepuff", 600))))

print(count_element(house_points, 600)) # 2

'''
Problem 3: Target Practice
You are practicing the accuracy of your spellwork by trying to extract the middle-most
ingredient in a line of potions. Given the head of a linked list, potions, use a
variation of the two-pointer technique to return the middle potion. If there are two
middle nodes, return the potion of the second middle node.

The two-pointer variation you should use is called the 'slow and fast pointer' or
'tortoise and the hare' technique. In this variation, a slow and a fast pointer are
incremented at different rates.

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.
'''

class Node:
	def __init__(self, potion, next=None):
		self.potion = potion
		self.next = next

def print_linked_list(head):
	current = head
	while current:
		print(current.potion, end=" -> " if current.next else "\n")
		current = current.next

def find_middle_potion(potions):
	pass

potions1 = Node("Poison Antidote", Node("Shrinking Solution", Node("Trollblood Tincture")))
potions2 = Node("Elixir of Life", Node("Sleeping Draught", Node("Babbling Beverage", Node("Aging Potion"))))

print(find_middle_potion(potions1)) # Shrinking Solution
print(find_middle_potion(potions2)) # Babbling Beverage

'''
Problem 4: Turn Back Time
A spell gone wrong has reversed time! Write a function reverse() that accepts the head
of a singly linked list events and restores order by reversing the order of elements.
Return the head of the reversed list.

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.
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

def reverse(events):
	pass

events = Node("Potion Brewing",
			Node("Spell Casting",
				Node("Wand Making",
					Node("Dragon Taming",
						Node("Broomstick Flying")))))

print_linked_list(reverse(events))
# Broomstick Flying -> Dragon Taming -> Wand Making -> Spell Casting -> Potion Brewing

'''
Problem 5: Mirror, Mirror
You think another bit of wonky spell casting may have left your enchanted mirror broken.
Write a function is_mirrored() to test if your mirror successfully reflects objects back.
The function accepts the head of a linked list and should return True if the values of
the linked list read the same backwards and forwards, and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.
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

def is_mirrored(head):
	pass

list1 = Node("Phoenix", Node("Dragon", Node("Phoenix")))
list2 = Node("Werewolf", Node("Vampire", Node("Griffin")))

print(is_mirrored(list1)) # True
print(is_mirrored(list2)) # False

'''
Problem 6: Magic Loop
In a nearby enchanted forest, magical paths sometimes loop back on themselves, creating
never-ending cycles. Write a function loop_start() to help you keep your way. The
function accepts the head of a linked list path_start and returns the value of the node
where the cycle starts. If the path has no cycle, return None.

A linked list has a cycle if, at some point in the list, the node's next pointer points
back to a previous node in the list.

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.
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

def loop_start(path_start):
	pass

path_start = Node("Mystic Falls")
waypoint1 = Node("Troll's Bridge")
waypoint2 = Node("Elven Arbor")
waypoint3 = Node("Fairy Glade")

path_start.next = waypoint1
waypoint1.next = waypoint2
waypoint2.next = waypoint3
waypoint3.next = waypoint1

print(loop_start(path_start)) # Troll's Bridge
