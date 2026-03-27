'''
Problem 1: Measuring Loop Length
As a trail worker, you've been tasked with measuring the length of a loop trail that
circles back to its starting point. Given the head of a linked list trailhead where each
node represents a trail marker and the last marker points back to the first marker,
return the length of the trail. Assume the length of the trail is equal to the number
of markers.

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def trail_length(trailhead):
	pass

marker1 = Node("Marker 1")
marker2 = Node("Marker 2")
marker3 = Node("Marker 3")
marker1.next = marker2
marker2.next = marker3
marker3.next = marker1

print(trail_length(marker1)) # 3

'''
Problem 2: Clearing the Path
While maintaining a trail, you discover that some parts of the path loop back on
themselves, creating confusing detours. Given the head of a linked list that may contain
cycles trailhead, write a function that removes any loops/cycles in the trail ensuring
a clear, straightforward path. Return the head of the cleared trail.

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing - careful this will cause an infinite loop when used on a list w/cycles
def print_linked_list(head):
	current = head
	while current:
		print(current.value, end=" -> " if current.next else "\n")
		current = current.next

def clear_trail(trailhead):
	pass

marker1 = Node("Trailhead")
marker2 = Node("Trail Fork")
marker3 = Node("The Falls")
marker4 = Node("Peak")
marker1.next = marker2
marker2.next = marker3
marker3.next = marker4
marker4.next = marker2

print_linked_list(clear_trail(marker1)) # Trailhead -> Trail Fork -> The Falls -> Peak

'''
Problem 3: Removing Duplicate Markers
When clearing an old trail, you notice some markers have been placed more than once,
confusing hikers. Given the head of a sorted linked list of numbered trail markers,
trailhead, write a function that removes all duplicate markers, keeping only the unique
ones. Return the head of the updated trail.
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

def remove_duplicate_markers(trailhead):
	pass

trailhead = Node(1, Node(2, Node(3, Node(3, Node(4)))))

print_linked_list(remove_duplicate_markers(trailhead)) # 1 -> 2 -> 4
# Explanation: 3 appears more than once so it is deleted from the list

'''
Problem 4: Controlled Burns
You are working with local foresters on a section of trail through local wilderness with
particularly dense forests. The foresters recommend doing controlled burns on certain
sections of the forest to help decrease severe wildfire risk and promote biodiversity,
which means certain parts of the trail will be off limits for the upcoming season. Given
the head of a linked list of trail markers, trailhead and two integers m and n, write a
function to traverse the trail, keeping only the first m markers, and then removing the
next n markers. Continue this pattern until the end of the trail is reached. Return the
head of the updated trail.
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

def selective_trail_clearing(trailhead, m, n):
	pass

trailhead = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))))

print_linked_list(selective_trail_clearing(trailhead, 2, 3)) # 1 -> 2 -> 6 -> 7 -> 11 -> 12
# Explanation: Keep the first (m = 2) nodes starting from the head of the linked list
# (1 -> 2). Delete the next (n = 3) nodes (3 -> 4 -> 5).
# Continue with the same procedure until reaching the tail of the linked list.

'''
Problem 5: Geocaching
You are hiking on a trail that has a geocache hidden at each marker. Each cache is also
labeled with a 0 or 1. The geocaches are arranged in a sequence, forming a binary code
that represents the coordinates of a special, hidden cache. The most significant bit is
at the first marker on the trail. Given the head of a linked list cache_labels
representing the sequence of 0s and 1s you found at each marker, write a function
locate_cache() that decodes the sequence and returns the decimal value of the hidden
cache's coordinates.
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

def locate_cache(cache_labels):
	pass

cache_labels = Node(1, Node(0, Node(1))) # 101 base 2

print(locate_cache(cache_labels)) # 5
# Explanation: (101) in base 2 = (5) in base 10

'''
Problem 6: Merging Trail Segments
While constructing a new trail, you've set up several segments separated by temporary
markers. Once the segments are ready, you want to merge them into continuous trails.
Given the head of a linked list of trail markers trailhead, merge the nodes between the
temporary markers (0s) by summing their values into a single marker. The final trail
should not contain any temporary markers. Return the head of the merged trail.

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

def merge_trail(trailhead):
	pass

trail1 = Node(0, Node(3, Node(1, Node(0, Node(4, Node(5, Node(2, Node(0))))))))
trail2 = Node(0, Node(1, Node(0, Node(3, Node(0, Node(2, Node(2, Node(0))))))))

print_linked_list(merge_trail(trail1)) # 4 -> 11
# Explanation: 3 + 1 = 4, 4 + 5 + 2 = 11
print_linked_list(merge_trail(trail2)) # 1 -> 3 -> 4
# Explanation: 1 = 1, 3 = 3, 2 + 2 = 4
