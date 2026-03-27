'''
Problem 1: Space Crew
Given two lists of length n, crew and position, map the space station crew to their position
on board the international space station.

Each crew member crew[i] has job position[i] on board, where 0 <= i < n and
len(crew) == len(position).
'''

def space_crew(crew, position):
	pass

exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", "Flight Engineer", "Flight Engineer"]
space_crew(exp70_crew, exp70_positions)
# {"Andreas Mogensen": "Commander", "Jasmin Moghbeli": "Flight Engineer",
#  "Satoshi Furukawa": "Flight Engineer", "Loral O'Hara": "Flight Engineer",
#  "Konstantin Borisov": "Flight Engineer"}

ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]
space_crew(ax3_crew, ax3_positions)
# {"Michael Lopez-Alegria": "Commander", "Walter Villadei": "Mission Pilot",
#  "Alper Gezeravci": "Mission Specialist", "Marcus Wandt": "Mission Specialist"}

'''
Problem 2: Space Encyclopedia
Given a dictionary planets that maps planet names to a dictionary containing the planet's
number of moons and orbital period, write a function planet_lookup() that accepts a string
planet_name and returns a string in the form:
"Planet <planet_name> has an orbital period of <orbital period> Earth days and has
<number of moons> moons."
If planet_name is not a key in planets, return "Sorry, I have no data on that planet.".
'''

def planet_lookup(planet_name):
	pass

planetary_info = {
	"Mercury": {"Moons": 0, "Orbital Period": 88},
	"Earth": {"Moons": 1, "Orbital Period": 365.25},
	"Mars": {"Moons": 2, "Orbital Period": 687},
	"Jupiter": {"Moons": 79, "Orbital Period": 10592}
}

planet_lookup("Jupiter")
# "Planet Jupiter has an orbital period of 10592 Earth days and has 79 moons."

planet_lookup("Pluto") # "Sorry, I have no data on that planet."

'''
Problem 3: Breathing Room
As part of your job as an astronaut, you need to perform routine safety checks. You are given
a dictionary oxygen_levels which maps room names to current oxygen levels and two integers
min_val and max_val specifying the acceptable range of oxygen levels. Return a list of room
names whose values are outside the range defined by min_val and max_val (inclusive).
'''

def check_oxygen_levels(oxygen_levels, min_val, max_val):
	pass

oxygen_levels = {
	"Command Module": 21,
	"Habitation Module": 20,
	"Laboratory Module": 19,
	"Airlock": 22,
	"Storage Bay": 18
}

min_val = 19
max_val = 22
check_oxygen_levels(oxygen_levels, min_val, max_val) # ['Storage Bay']

'''
Problem 4: Experiment Analysis
Write a function data_difference() that accepts two dictionaries experiment1 and experiment2
and returns a new dictionary that contains only key-value pairs found exclusively in
experiment1 but not in experiment2.
'''

def data_difference(experiment1, experiment2):
	pass

exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}
data_difference(exp1_data, exp2_data) # {'temperature': 22, 'humidity': 45}

'''
Problem 5: Name the Node
NASA has asked the public to vote on a new name for one of the nodes in the International
Space Station. Given a list of strings votes where each string is a voter's suggested new
name, implement a function get_winner() that returns the suggestion with the most votes.

If there is a tie, return either option.
'''

def get_winner(votes):
	pass

votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
get_winner(votes1) # "Colbert"

votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]
get_winner(votes2) # "Colbert" or "Serenity" (tie — either is acceptable)

'''
Problem 6: Check if the Transmission is Complete
Ground control has sent a transmission containing important information. A complete
transmission is one where every letter of the English alphabet appears at least once.

Given a string transmission containing only lowercase English letters, return True if the
transmission is complete, or False otherwise.
'''

def check_if_complete_transmission(transmission):
	pass

transmission1 = "thequickbrownfoxjumpsoverthelazydog"
check_if_complete_transmission(transmission1) # True

transmission2 = "spacetravel"
check_if_complete_transmission(transmission2) # False

'''
Problem 7: Signal Pairs
Ground control is analyzing signal patterns received from different probes. You are given a
0-indexed array signals consisting of distinct strings.

The string signals[i] can be paired with the string signals[j] if signals[i] is equal to the
reversed string of signals[j], where 0 <= i < j < len(signals). Return the maximum number of
pairs that can be formed from the array signals.

Note that each string can belong in at most one pair.
'''

def max_number_of_string_pairs(signals):
	pass

signals1 = ["cd", "ac", "dc", "ca", "zz"]
max_number_of_string_pairs(signals1) # 2

signals2 = ["ab", "ba", "cc"]
max_number_of_string_pairs(signals2) # 1

signals3 = ["aa", "ab"]
max_number_of_string_pairs(signals3) # 0

'''
Problem 8: Find the Difference of Two Signal Arrays
You are given two 0-indexed integer arrays signals1 and signals2, representing signal data
from two different probes. Return a list answer of size 2 where:

answer[0] is a list of all distinct integers in signals1 which are not present in signals2.
answer[1] is a list of all distinct integers in signals2 which are not present in signals1.

Note that the integers in the lists may be returned in any order.

Below is the pseudocode for the problem. Implement this in Python and explain your
implementation step-by-step.

1. Convert signals1 and signals2 to sets.
2. Find the difference between set1 and set2 and store it in diff1.
3. Find the difference between set2 and set1 and store it in diff2.
4. Return the list [diff1, diff2].
'''

def find_difference(signals1, signals2):
	pass

signals1_ex1 = [1, 2, 3]
signals2_ex1 = [2, 4, 6]
find_difference(signals1_ex1, signals2_ex1) # [[1, 3], [4, 6]]

signals1_ex2 = [1, 2, 3, 3]
signals2_ex2 = [1, 1, 2, 2]
find_difference(signals1_ex2, signals2_ex2) # [[3], []]

'''
Problem 9: Common Signals Between Space Probes
Two space probes have collected signals represented by integer arrays signals1 and signals2
of sizes n and m, respectively. Calculate the following values:

answer1: the number of indices i such that signals1[i] exists in signals2.
answer2: the number of indices j such that signals2[j] exists in signals1.

Return [answer1, answer2].
'''

def find_common_signals(signals1, signals2):
	pass

signals1_ex1 = [2, 3, 2]
signals2_ex1 = [1, 2]
find_common_signals(signals1_ex1, signals2_ex1) # [2, 1]

signals1_ex2 = [4, 3, 2, 3, 1]
signals2_ex2 = [2, 2, 5, 2, 3, 6]
find_common_signals(signals1_ex2, signals2_ex2) # [3, 4]

signals1_ex3 = [3, 4, 2, 3]
signals2_ex3 = [1, 5]
find_common_signals(signals1_ex3, signals2_ex3) # [0, 0]

'''
Problem 10: Common Signals Between Space Probes II
If you implemented find_common_signals() in the previous problem using dictionaries, try
reimplementing the function using sets instead. If you used sets, use dictionaries this time.

Once you've come up with your second solution, compare the two. Is one solution better than
the other? How so? Why or why not?
'''

def find_common_signals(signals1, signals2):
	pass

signals1_ex1 = [2, 3, 2]
signals2_ex1 = [1, 2]
find_common_signals(signals1_ex1, signals2_ex1) # [2, 1]

signals1_ex2 = [4, 3, 2, 3, 1]
signals2_ex2 = [2, 2, 5, 2, 3, 6]
find_common_signals(signals1_ex2, signals2_ex2) # [3, 4]

signals1_ex3 = [3, 4, 2, 3]
signals2_ex3 = [1, 5]
find_common_signals(signals1_ex3, signals2_ex3) # [0, 0]

'''
Problem 11: Sort Signal Data
Ground control needs to analyze the frequency of signal data received from different probes.
Given an array of integers signals, sort the array in increasing order based on the frequency
of the values. If multiple values have the same frequency, sort them in decreasing order.
Return the sorted array.

Below is a buggy or incomplete version of the solution. Identify and fix the bugs in the
code. Then, perform a code review and suggest improvements.
'''

def frequency_sort(signals):
	freq = {}
	for signal in signals:
		if signal in freq:
			freq[signal] += 1
		else:
			freq[signal] = 0

	sorted_signals = sorted(signals, key=lambda x: (freq[x], x))

	return sorted_signals

signals1 = [1, 1, 2, 2, 2, 3]
frequency_sort(signals1) # [3, 1, 1, 2, 2, 2]

signals2 = [2, 3, 1, 3, 2]
frequency_sort(signals2) # [1, 3, 3, 2, 2]

signals3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
frequency_sort(signals3) # [5, -1, 4, 4, -6, -6, 1, 1, 1]

'''
Problem 12: Final Communication Hub
You are given an array paths, where paths[i] = [hubA, hubB] means there exists a direct
communication path going from hubA to hubB. Return the final communication hub, that is,
the hub without any outgoing path to another hub.

It is guaranteed that the paths form a line without any loops, therefore, there will be
exactly one final communication hub.
'''

def find_final_hub(paths):
	pass

paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
find_final_hub(paths1) # "Europa"

paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
find_final_hub(paths2) # "Delta"

paths3 = [["StationA", "StationZ"]]
find_final_hub(paths3) # "StationZ"
