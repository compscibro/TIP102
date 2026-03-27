'''
Problem 1: Final Costs After a Supply Discount
You are managing the budget for a global expedition, where the cost of supplies is
represented by an integer array costs, where costs[i] is the cost of the ith supply item.

There is a special discount available during the expedition. If you purchase the ith item,
you will receive a discount equivalent to costs[j], where j is the minimum index such that
j > i and costs[j] <= costs[i]. If no such j exists, you will not receive any discount.

Return an integer array final_costs where final_costs[i] is the final cost you will pay for
the ith supply item, considering the special discount.
'''

def final_supply_costs(costs):
	pass

final_supply_costs([8, 4, 6, 2, 3]) # [4, 2, 4, 2, 3]
final_supply_costs([1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
final_supply_costs([10, 1, 1, 6]) # [9, 0, 1, 6]

'''
Problem 2: Find First Symmetrical Landmark Name
During your global expedition, you encounter a series of landmarks, each represented by a
string in the array landmarks. Your task is to find and return the first symmetrical landmark
name. If there is no such name, return an empty string "".

A landmark name is considered symmetrical if it reads the same forward and backward.
'''

def first_symmetrical_landmark(landmarks):
	pass

first_symmetrical_landmark(["canyon", "forest", "rotor", "mountain"]) # "rotor"
first_symmetrical_landmark(["plateau", "valley", "cliff"]) # ""

'''
Problem 3: Terrain Elevation Match
During your global expedition, you are mapping out the terrain elevations, where the
elevation of each point is represented by an integer. You are given a string terrain of
length n, where:

terrain[i] == 'I' indicates that the elevation at the ith point is lower than the elevation
at the i+1th point (elevation[i] < elevation[i + 1]).
terrain[i] == 'D' indicates that the elevation at the ith point is higher than the elevation
at the i+1th point (elevation[i] > elevation[i + 1]).

Your task is to reconstruct the elevation sequence and return it as a list of integers. If
there are multiple valid sequences, return any of them.

Hint: Try using two variables: one to track the smallest available number and one for the
largest. As you process each character in the string, assign the smallest number when the
next elevation should increase ('I'), and assign the largest number when the next elevation
should decrease ('D').
'''

def terrain_elevation_match(terrain):
	pass

terrain_elevation_match("IDID") # [0, 4, 1, 3, 2]
terrain_elevation_match("III") # [0, 1, 2, 3]
terrain_elevation_match("DDI") # [3, 2, 0, 1]

'''
Problem 4: Find the Expedition Log Concatenation Value
You are recording journal entries during a global expedition, where each entry is represented
by a 0-indexed integer array logs. The concatenation of two journal entries means combining
their numerals into one. For example, concatenating 15 and 49 results in 1549.

Your task is to calculate the total concatenation value of all the journal entries, which
starts at 0. To do this, perform the following steps until no entries remain:

- If there are at least two entries in the logs, concatenate the first and last entries, add
  the result to the current concatenation value, and then remove these two entries.
- If there is only one entry left, add its value to the concatenation value and remove it.

Repeat until the array logs is empty. Return the final concatenation value.
'''

def find_the_log_conc_val(logs):
	pass

find_the_log_conc_val([7, 52, 2, 4]) # 596
find_the_log_conc_val([5, 14, 13, 8, 12]) # 673

'''
Problem 5: Number of Explorers Unable to Gather Supplies
During a global expedition, explorers must gather supplies from a limited stockpile, which
includes two types of resources: type 0 (e.g., food rations) and type 1 (e.g., medical
kits). The explorers are lined up in a queue, each with a specific preference for one of the
two types of resources.

The number of supplies in the stockpile is equal to the number of explorers. The supplies
are stacked in a pile. At each step:

- If the explorer at the front of the queue prefers the resource on the top of the stack,
  they will take it and leave the queue.
- Otherwise, they will leave the resource and go to the end of the queue.

This process continues until no explorer in the queue wants to take the top resource, leaving
some explorers unable to gather the supplies they need.

You are given two integer arrays explorers and supplies, where supplies[i] is the type of
the ith resource in the stack (i = 0 is the top of the stack) and explorers[j] is the
preference of the jth explorer in the initial queue (j = 0 is the front of the queue).
Return the number of explorers that are unable to gather their preferred supplies.
'''

def count_explorers(explorers, supplies):
	pass

count_explorers([1, 1, 0, 0], [0, 1, 0, 1]) # 0
count_explorers([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]) # 3

'''
Problem 6: Count Balanced Terrain Subsections
During your global expedition, you are analyzing a binary terrain string, terrain, where 0
represents a valley and 1 represents a hill. You need to count the number of non-empty
balanced subsections in the terrain. A balanced subsection is defined as a contiguous segment
of the terrain where an equal number of valleys (0s) and hills (1s) appear, and all the 0s
and 1s are grouped consecutively.

Return the total number of these balanced subsections. Note that subsections that occur
multiple times should be counted each time they appear.
'''

def count_balanced_terrain_subsections(terrain):
	pass

count_balanced_terrain_subsections("00110011") # 6
count_balanced_terrain_subsections("10101") # 4

'''
Problem 7: Check if a Signal Occurs as a Prefix in Any Transmission
During your global expedition, you are monitoring various transmissions, each consisting of
some signals separated by a single space. You are given a searchSignal and need to check if
it occurs as a prefix to any signal in a transmission.

Return the index of the signal in the transmission (1-indexed) where searchSignal is a
prefix of this signal. If searchSignal is a prefix of more than one signal, return the index
of the first signal (minimum index). If there is no such signal, return -1.

A prefix of a string s is any leading contiguous substring of s.
'''

def is_prefix_of_signal(transmission, searchSignal):
	pass

is_prefix_of_signal("i love eating burger", "burg") # 4
is_prefix_of_signal("this problem is an easy problem", "pro") # 2
is_prefix_of_signal("i am tired", "you") # -1
