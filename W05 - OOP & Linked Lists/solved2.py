# 6 7

# Problem 1: Mutual Friends

# In the Villager class below, each villager has a friends attribute, 
# which is a list of other villagers they are friends with.

# Write a method get_mutuals() that takes one parameter, a Villager instance new_contact, 
# and returns a list with the name of all friends the current villager and new_contact have in common.

"""
Understand:
- Return a list with all friends that both have in common
- Current object, villager bject other

Match:
Object methods

Plan:
1. Access self friends
2. Access new contact friends
3. Return set intersection of both

Time & Space Complexity:
O(n) - New List Creation for Time
O(n) - New List Creation for Spac
"""

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        res = []
        current_friends = set(self.friends)
        new_contact_friends = set(new_contact.friends)
        intersection = list(current_friends & new_contact_friends)
        for intersect in intersection:
            res.append(intersect.name)

        return res


# tests

"""
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
"""

"""
A linked list is a data structure that, similar to a normal list or array, 
allows us to store pieces of data sequentially. 
The key difference is how the elements are stored in memory.

In a normal list, elements are stored in adjacent memory locations. 
If we know the location of the first element, 
we can easily access any other element in the list.

In a linked list, individual elements, called nodes, 
are not stored in sequential memory locations. 
Instead, each node stores a reference or pointer to the next node in the list, 
allowing us to traverse the list.

Connect the provided node instances below to create 
the linked list kk_slider -> harriet -> saharah -> isabelle.

A function print_linked_list() which accepts the head, 
or first element, of a linked list and prints the values of the 
list has also been provided for testing purposes.

Understand: 
Given the nodes, update the next pointers and debut using the given debug method
Match:
Singly Linked List
Plan:
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
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
Imagine a linked list used as a daily task list where each node represents a task. 
Write a function add_task() that takes in the head of a linked list and adds a new 
node to the front of the task list.

The function should insert a new Node object with the value task as the new head 
of the linked list and return the new node.

Note: The "head" of a linked list is the first element in the linked list. 
It is equivalent to lst[0] of a normal list.
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def add_first(head, task):
    newHead = Node(task)
    # oldHead = head
    newHead.next = head

    return newHead

task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices")) # check turnip prices -> shake tree -> dig fossils -> catch bugs

'''
Write a function halve_list() that accepts the head of a linked list 
whose values are integers and divides each value by two. 
Return the head of the modified list.
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def halve_list(head):
    current = head
    while current:
        if current.value :
            current.value = current.value / 2
        current = current.next
    return head

node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one)) # 2.5  -> 3 -> 3.5

'''
Write a function delete_tail() that accepts the head of a linked list 
and removes the last node in the list. Return the head of the modified list.

Note: The "tail" of a list is the last element in the linked list. 
It is equivalent to lst[-1] in a normal list.
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_tail(head):
    
    # Only one node in linked list
    if not head.next:
        return None

    # Iterate through more than one node  
    current = head
    while current.next.next: 
        current = current.next
    current.next = None
    return head



butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))

'''
Write a function find_min() that takes in the head of a linked list and 
returns the minimum value in the linked list. You can assume the linked list
will contain only numeric values.
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_min(head):
    minimum = float('inf')

    current = head
    while current: 
        if current.value < minimum: 
            minimum = current.value

        current = current.next

    return minimum 


head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
print(find_min(head2))


'''
Imagine a linked list used to store a player's inventory. 
Write a function delete_item() that takes in the head of a 
linked list and a value item as parameters.

The function should remove the first node it finds in the 
linked list with the value item and return the head of the 
modified list. If no node can be found with the value item, 
return the list unchanged.

Current item is value we're removing -> Create temp value to store current.next
return current.next

1. Check if the current.next.value = item
2. Create temp with next.next if exists, if not None
3. current.next = temp
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_item(head, item):
    if head.value == item:
        temp = Node(head.next.value, head.next.next)
        head.next = None
        return temp

    while current.next:
        
    pass

slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))

# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))