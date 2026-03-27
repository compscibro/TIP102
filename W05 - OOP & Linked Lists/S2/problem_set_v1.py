'''
Problem 1: Mutual Friends
In the Villager class below, each villager has a friends attribute, which is a list of other
villagers they are friends with.

Write a method get_mutuals() that takes one parameter, a Villager instance new_contact, and
returns a list with the name of all friends the current villager and new_contact have in common.
'''

class Villager:
	def __init__(self, name, species, catchphrase):
		self.name = name
		self.species = species
		self.catchphrase = catchphrase
		self.friends = []

	def get_mutuals(self, new_contact):
		pass

bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal)) # ['Raymond', 'Fauna']

ankha.friends = [marshal]
print(bob.get_mutuals(ankha)) # []

'''
Problem 2: Linked Up
A linked list is a data structure that, similar to a normal list or array, allows us to store
pieces of data sequentially. The key difference is how the elements are stored in memory.

In a normal list, elements are stored in adjacent memory locations. If we know the location of
the first element, we can easily access any other element in the list.

In a linked list, individual elements, called nodes, are not stored in sequential memory
locations. Instead, each node stores a reference or pointer to the next node in the list,
allowing us to traverse the list.

Connect the provided node instances below to create the linked list
kk_slider -> harriet -> saharah -> isabelle.

A function print_linked_list() which accepts the head, or first element, of a linked list and
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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

print_linked_list(kk_slider) # K.K. Slider -> Harriet -> Saharah -> Isabelle

'''
Problem 3: Daily Tasks
Imagine a linked list used as a daily task list where each node represents a task. Write a
function add_first() that takes in the head of a linked list and adds a new node to the front
of the task list.

The function should insert a new Node object with the value task as the new head of the linked
list and return the new node.

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

def add_first(head, task):
	pass

task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

print_linked_list(add_first(task_1, "check turnip prices"))
# check turnip prices -> shake tree -> dig fossils -> catch bugs

'''
Problem 4: Halve List
Write a function halve_list() that accepts the head of a linked list whose values are integers
and divides each value by two. Return the head of the modified list.
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

def halve_list(head):
	pass

node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

print_linked_list(halve_list(node_one)) # 2.5 -> 3 -> 3.5

'''
Problem 5: Remove Last
Write a function delete_tail() that accepts the head of a linked list and removes the last node
in the list. Return the head of the modified list.

Note: The "tail" of a list is the last element in the linked list. It is equivalent to lst[-1]
in a normal list.
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

def delete_tail(head):
	pass

butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

print_linked_list(delete_tail(butterfly)) # Common Butterfly -> Ladybug

'''
Problem 6: Find Minimum in Linked List
Write a function find_min() that takes in the head of a linked list and returns the minimum
value in the linked list. You can assume the linked list will contain only numeric values.
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

def find_min(head):
	pass

head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

print(find_min(head1)) # 5
print(find_min(head2)) # 5

'''
Problem 7: Remove From Inventory
Imagine a linked list used to store a player's inventory. Write a function delete_item() that
takes in the head of a linked list and a value item as parameters.

The function should remove the first node it finds in the linked list with the value item and
return the head of the modified list. If no node can be found with the value item, return the
list unchanged.
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

def delete_item(head, item):
	pass

slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

print_linked_list(delete_item(slingshot, "Peaches")) # Slingshot -> Scarab Beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso")) # Slingshot -> Scarab Beetle

'''
Problem 8: Move Tail to Front of Linked List
Write a function tail_to_head() that takes in the head of a linked list as a parameter and
moves the tail of the linked list to the front.
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

def tail_to_head(head):
	pass

daisy = Node("Daisy")
mario = Node("Mario")
toad = Node("Toad")
peach = Node("Peach")
daisy.next = mario
mario.next = toad
toad.next = peach

print_linked_list(tail_to_head(daisy)) # Peach -> Daisy -> Mario -> Toad

'''
Problem 9: Create Double Links
One of the drawbacks of a linked list is that it's difficult to go backwards because each Node
only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly
linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Update the Node constructor below so that the code creates a doubly linked list with
head <-> tail.
'''

class Node:
	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev

head = Node("Isabelle")
tail = Node("K.K. Slider")

head.next = tail
tail.prev = head

print(head.value, "<->", head.next.value) # Isabelle <-> K.K. Slider
print(tail.prev.value, "<->", tail.value) # Isabelle <-> K.K. Slider

'''
Problem 10: Print Backwards
Write a function print_reverse() that takes in the tail of a doubly linked list as a parameter.

It should print out the values of the linked list in reverse order, each separated by a space.
'''

class Node:
	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev

def print_reverse(tail):
	pass

isabelle = Node("Isabelle")
kk_slider = Node("K.K. Slider")
saharah = Node("Saharah")
isabelle.next = kk_slider
kk_slider.next = saharah
saharah.prev = kk_slider
kk_slider.prev = isabelle

print_reverse(saharah) # Saharah K.K. Slider Isabelle
