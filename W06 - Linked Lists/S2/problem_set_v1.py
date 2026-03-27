'''
Problem 1: Wild Goose Chase
You're a detective and have been given an anonymous tip on your latest case, but
something about it seems fishy - you suspect the clue might be a red herring meant to
send you around in circles. Write a function is_circular() that accepts the head of a
singly linked list clues and returns True if the tail of the linked list points at the
head of the linked list. Otherwise, return False.

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def is_circular(clues):
	pass

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1)) # True

'''
Problem 2: Breaking the Cycle
All the clues that lead us in circles are false evidence we need to purge! Given the
head of a linked list evidence, clean up the evidence list by identifying any false
clues. Write a function collect_false_evidence() that returns an array containing all
values that are part of any cycle in evidence. Return the values in any order.

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def collect_false_evidence(evidence):
	pass

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
# ['The stolen goods are at an abandoned warehouse', 'The mayor is accepting bribes', 'They dumped their disguise in the lake']
print(collect_false_evidence(clue5)) # []

'''
Problem 3: Prioritizing Suspects
You've identified a list of suspects, but time is limited and you won't be able to
question all of them today. Write a function partition() to help prioritize the order
in which you question suspects. Given the head of a linked list of integers
suspect_ratings, where each integer represents the suspiciousness of a given suspect
and a value threshold, partition the linked list such that all nodes with values greater
than threshold come before nodes with values less than or equal to threshold.

Return the head of the partitioned list.

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

def partition(suspect_ratings, threshold):
	pass

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3)) # 4 -> 5 -> 1 -> 3 -> 2 -> 2
# Note: nodes 4 and 5 can be in any order so long as they come before 3, 2, and 1.
# 5 -> 4 -> 3 -> 1 -> 2 -> 2 would also be an acceptable answer.

'''
Problem 4: Puzzling it Out
A new witness has emerged and provided a new account of events the night of the crime.
Given the heads of two sorted linked lists, known_timeline and witness_timeline, each
representing a numbered sequence of events, merge the two timelines into one sorted
sequence of events. The resulting linked list should be made by splicing together the
nodes of the first two timelines. Return the head of the merged timeline.

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

def merge_timelines(known_timeline, witness_timeline):
	pass

known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))

print_linked_list(merge_timelines(known_timeline, witness_timeline)) # 1 -> 1 -> 2 -> 3 -> 4 -> 4

'''
Problem 5: A New Perspective
You're having a tough time making a break in the case, and it's time to shake things up
to gain a new perspective. Given the head of a linked list of numbered pieces of evidence
evidence, and a non-negative integer k, rotate the list to the right by k places. Return
the head of the rotated list.

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

def rotate_right(evidence, k):
	pass

evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
evidence_list2 = Node(0, Node(1, Node(2)))

print_linked_list(rotate_right(evidence_list1, 2)) # 4 -> 5 -> 1 -> 2 -> 3
print_linked_list(rotate_right(evidence_list2, 4)) # 2 -> 0 -> 1

'''
Problem 6: Adding Up the Evidence
You have all your evidence, and it's time to sum it to the final answer! You are given
the heads of two non-empty linked lists head_a and head_b representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the sum as a linked list.

The digits of the sum should also be stored in reverse order with each node containing
a single digit.

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

def add_two_numbers(head_a, head_b):
	pass

head_a = Node(2, Node(4, Node(3))) # 342
head_b = Node(5, Node(6, Node(4))) # 465

print_linked_list(add_two_numbers(head_a, head_b)) # 7 -> 0 -> 8
# Explanation: 342 + 465 = 807
