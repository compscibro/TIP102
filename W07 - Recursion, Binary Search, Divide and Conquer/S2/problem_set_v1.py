'''
Problem 1: Finding the Perfect Cruise
It's vacation time! Given an integer vacation_length and a list of integers
cruise_lengths sorted in ascending order, use binary search to return True if there is
a cruise length that matches vacation_length and False otherwise.
'''

def find_cruise_length(cruise_lengths, vacation_length):
	pass

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13)) # True
print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11)) # False

'''
Problem 2: Booking the Perfect Cruise Cabin
As part of your cruise planning, you have a list of available cabins sorted in ascending
order by their deck level. Given the list of available cabins represented by deck level,
cabins, and an integer preferred_deck, write a recursive function find_cabin_index()
that returns the index of preferred_deck. If a cabin with your preferred_deck does not
exist in cabins, return the index where it would be if it were added to the list to
maintain the sorted order.

Your algorithm must have O(log n) time complexity.
'''

def find_cabin_index(cabins, preferred_deck):
	pass

print(find_cabin_index([1, 3, 5, 6], 5)) # 2
print(find_cabin_index([1, 3, 5, 6], 2)) # 1
print(find_cabin_index([1, 3, 5, 6], 7)) # 4

'''
Problem 3: Count Checked In Passengers
As a cruise ship worker, you're in charge of tracking how many passengers have checked
in to their rooms thus far. You are given a list of rooms where passengers are either
checked in (represented by a 1) or not checked in (represented by a 0). The list is
sorted, so all the 0s appear before any 1s.

Write a function count_checked_in_passengers() that efficiently counts and returns the
total number of checked-in passengers (1s) in the list in O(log n) time.
'''

def count_checked_in_passengers(rooms):
	pass

rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1)) # 4
print(count_checked_in_passengers(rooms2)) # 1
print(count_checked_in_passengers(rooms3)) # 0

'''
Problem 4: Determining Profitability of Excursions
As the activities director on a cruise ship, you're organizing excursions for the
passengers. You have a sorted list of non-negative integers excursion_counts, where each
number represents the number of passengers who have signed up for various excursions at
your next cruise destination. The list is considered profitable if there exists a number
x such that there are exactly x excursions that have at least x passengers signed up.

Write a function that determines whether excursion_counts is profitable. If it is
profitable, return the value of x. If it is not profitable, return -1. It can be proven
that if excursion_counts is profitable, the value for x is unique.

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.
'''

def is_profitable(excursion_counts):
	pass

print(is_profitable([3, 5])) # 2
# Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
print(is_profitable([0, 0])) # -1
# Explanation: No numbers fit the criteria for x.

'''
Problem 5: Finding the Shallowest Point
As the captain of the cruise ship, you need to take a detour to steer clear of an
incoming storm. Given an array of integers depths representing the varying water depths
along your potential new route, write a function find_shallowest_point() to help you
decide whether the new route is deep enough for your ship. The function should use a
divide-and-conquer approach to return the shallowest point (minimum value) in depths.
You may not use the built-in min() function.

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.
'''

def find_shallowest_point(depths):
	pass

print(find_shallowest_point([5, 7, 2, 8, 3])) # 2
print(find_shallowest_point([12, 15, 10, 21])) # 10

'''
Problem 6: Cruise Ship Treasure Hunt
As a fun game, the cruise ship director has organized a treasure hunt for the kids on
board and hidden a chest of candy in one of the rooms on board. The rooms are organized
in a m x n grid, where each row and each column are sorted in ascending order by room
number. Given an integer representing the room number where the prize is hidden
treasure, use a divide and conquer approach to return a tuple in the form (row, col)
representing the row and column indices where treasure was found. If treasure is not in
the matrix, return (-1, -1).

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.
'''

def find_treasure(matrix, treasure):
	pass

rooms = [
	[1, 4, 7, 11],
	[8, 9, 10, 20],
	[11, 12, 17, 30],
	[18, 21, 23, 40]
]

print(find_treasure(rooms, 17)) # (2, 2)
print(find_treasure(rooms, 5)) # (-1, -1)
