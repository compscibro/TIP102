'''
Problem 1: Calculating Village Size
In the kingdom of Codepathia, the queen determines how many resources to distribute to
a village based on its class. A village's class is equal to the number of digits in its
population. Given an integer population, write a function get_village_class() that
returns the number of digits in population.

Implement the solution iteratively.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
'''

def get_village_class_iterative(population):
	pass

def get_village_class_recursive(population):
	pass

print(get_village_class_iterative(432)) # 3
print(get_village_class_recursive(432)) # 3
print(get_village_class_iterative(9)) # 1
print(get_village_class_recursive(9)) # 1

'''
Problem 2: Counting the Castle Walls
In a faraway kingdom, a castle is surrounded by multiple defensive walls, where each
wall is nested within another. Given a list of lists walls where each list [] represents
a wall, write a recursive function count_walls() that returns the total number of walls.

Evaluate the time complexity of your solution. Define your variables and provide a
rationale for why you believe your solution has the stated time complexity.
'''

def count_walls(walls):
	pass

walls = ["outer", ["inner", ["keep", []]]]

print(count_walls(walls)) # 4
print(count_walls([])) # 1

'''
Problem 3: Reversing a Scroll
A wizard is deciphering an ancient scroll and needs to reverse the letters in a word to
reveal a hidden message. Write a recursive function to reverse the letters in a given
scroll and returns the reversed scroll. Assume scroll only contains alphabetic
characters.

Evaluate the time complexity of your solution. Define your variables and provide a
rationale for why you believe your solution has the stated time complexity.
'''

def reverse_scroll(scroll):
	pass

print(reverse_scroll("cigam")) # magic
print(reverse_scroll("lleps")) # spell

'''
Problem 4: Palindromic Name
Queen Ada is superstitious and believes her children will only have good fortune if
their name is symmetrical and reads the same forward and backward. Write a recursive
function that takes in a string comprised of only lowercase alphabetic characters name
and returns True if the name is palindromic and False otherwise.

Evaluate the time complexity of your solution. Define your variables and provide a
rationale for why you believe your solution has the stated time complexity.
'''

def is_palindrome(name):
	pass

print(is_palindrome("eve")) # True
print(is_palindrome("ling")) # False
print(is_palindrome("")) # True

'''
Problem 5: Doubling the Power of a Spell
The court magician is practicing a spell that doubles its power with each incantation.
Given an integer initial_power and a non-negative integer n, write a recursive function
that doubles initial_power n times.

Evaluate the time complexity of your solution. Define your variables and provide a
rationale for why you believe your solution has the stated time complexity.
'''

def double_power(initial_power, n):
	pass

print(double_power(5, 3)) # 40
# Explanation: 5 doubled 3 times: 5 -> 10 -> 20 -> 40
print(double_power(7, 2)) # 28
# Explanation: 7 doubled 2 times: 7 -> 14 -> 28

'''
Problem 6: Checking the Knight's Path
A knight is traveling along a path marked by stones, and each stone has a number on it.
The knight must check if the numbers on the stones form a strictly increasing sequence.
Write a recursive function to determine if the sequence is strictly increasing.

Evaluate the time complexity of your solution. Define your variables and provide a
rationale for why you believe your solution has the stated time complexity.
'''

def is_increasing_path(path):
	pass

print(is_increasing_path([1, 2, 3, 4, 5])) # True
print(is_increasing_path([3, 5, 2, 8])) # False

'''
Problem 7: Finding the Longest Winning Streak
In the kingdom's grand tournament, knights compete in a series of challenges. A knight's
performance in the challenge is represented by a string challenges, where a success is
represented by an S and each other outcome (like a draw or loss) is represented by an
"O". Write a recursive function to find the length of the longest consecutive streak of
successful challenges ("S").

Evaluate the time complexity of your solution. Define your variables and provide a
rationale for why you believe your solution has the stated time complexity.
'''

def longest_streak(challenges, current_length=0, max_length=0):
	pass

print(longest_streak("SSOSSS")) # 3
print(longest_streak("SOSOSOSO")) # 1

'''
Problem 8: Weaving Spells
A magician can double a spell's power if they merge two incantations together. Given the
heads of two linked lists spell_a and spell_b where each node in the lists contains a
spell segment, write a recursive function weave_spells() that weaves spells in the
pattern:

a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...
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

def weave_spells(spell_a, spell_b):
	pass

spell_a = Node('A', Node('C', Node('E')))
spell_b = Node('B', Node('D', Node('F')))

print_linked_list(weave_spells(spell_a, spell_b)) # A -> B -> C -> D -> E -> F

'''
Problem 9: Weaving Spells II
Below is an iterative solution to the weave_spells() function from the previous
problem. Compare your recursive solution to the iterative solution below.

Discuss with your podmates. Which solution do you prefer?
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

def weave_spells(spell_a, spell_b):
	# If either list is empty, return the other
	if not spell_a:
		return spell_b
	if not spell_b:
		return spell_a

	# Start with the first node of spell_a
	head = spell_a

	# Loop through both lists until one is exhausted
	while spell_a and spell_b:
		# Store the next pointers
		next_a = spell_a.next
		next_b = spell_b.next

		# Weave spell_b after spell_a
		spell_a.next = spell_b

		# If there's more in spell_a, weave it after spell_b
		if next_a:
			spell_b.next = next_a

		# Move to the next nodes
		spell_a = next_a
		spell_b = next_b

	# Return the head of the new woven list
	return head
