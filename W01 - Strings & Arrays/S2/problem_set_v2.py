'''
Problem 1: String Array Equivalency
Given two string arrays word1 and word2, return True if the two arrays represent the same
string, and False otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
'''

def are_equivalent(word1, word2):
	pass

word1 = ["bat", "man"]
word2 = ["b", "atman"]
are_equivalent(word1, word2) # True

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
are_equivalent(word1, word2) # False

word1 = ["cat", "wom", "an"]
word2 = ["catwoman"]
are_equivalent(word1, word2) # True

'''
Problem 2: Count Even Strings
Implement a function count_evens() that accepts a list of strings lst as a parameter. The
function should return the number of strings with an even length in the list.
'''

def count_evens(lst):
	pass

lst = ["na", "nana", "nanana", "batman", "!"]
count_evens(lst) # 4

lst = ["the", "joker", "robin"]
count_evens(lst) # 0

lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
count_evens(lst) # 9

'''
Problem 3: Secret Identity
Write a function remove_name() to keep Batman's secret identity hidden. The function accepts
a list of names people and a string secret_identity and should return the list with any
instances of secret_identity removed. The list must be modified in place; you may not create
any new lists as part of your solution. Relative order of the remaining elements must be
maintained.
'''

def remove_name(people, secret_identity):
	pass

people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
remove_name(people, secret_identity) # ['Batman', 'Superman', 'The Riddler']

'''
Problem 4: Count Digits
Given a non-negative integer n, write a function count_digits() that returns the number of
digits in n. You may not cast n to a string.
'''

def count_digits(n):
	pass

n = 964
count_digits(n) # 3

n = 0
count_digits(n) # 1

'''
Problem 5: Move Zeroes
Write a function move_zeroes() that accepts an integer array nums and returns a new list with
all 0s moved to the end of the list. The relative order of the non-zero elements in the
original list should be maintained.
'''

def move_zeroes(lst):
	pass

lst = [1, 0, 2, 0, 3, 0]
move_zeroes(lst) # [1, 2, 3, 0, 0, 0]

'''
Problem 6: Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper
cases and more than once.
'''

def reverse_vowels(s):
	pass

s = "robin"
reverse_vowels(s) # "ribon"

s = "BATgirl"
reverse_vowels(s) # "BiTgArl"

s = "batman"
reverse_vowels(s) # "batman"

'''
Problem 7: Vantage Point
Batman is going on a scouting trip, surveying an area where he thinks Harley Quinn might
commit her next crime spree. The area has many hills with different heights and Batman wants
to find the tallest one to get the best vantage point. His scout trip consists of n + 1
points at different altitudes. Batman starts his trip at point 0 with altitude 0.

Write a function highest_altitude() that accepts an integer array gain of length n where
gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n).
Return the highest altitude of a point.
'''

def highest_altitude(gain):
	pass

gain = [-5, 1, 5, 0, -7]
highest_altitude(gain) # 1

gain = [-4, -3, -2, -1, 4, 3, 2]
highest_altitude(gain) # 0

'''
Problem 8: Left and Right Sum Differences
Given a 0-indexed integer array nums, write a function left_right_difference() that returns
a 0-indexed integer array answer where:

len(answer) == len(nums)
answer[i] = left_sum[i] - right_sum[i]

Where:
left_sum[i] is the sum of elements to the left of index i in nums. If there is no such
element, left_sum[i] = 0.
right_sum[i] is the sum of elements to the right of index i in nums. If there is no such
element, right_sum[i] = 0.
'''

def left_right_difference(nums):
	pass

nums = [10, 4, 8, 3]
left_right_difference(nums) # [-15, -1, 11, 22]

nums = [1]
left_right_difference(nums) # [0]

'''
Problem 9: Common Cause
Write a function common_elements() that takes in two lists lst1 and lst2 and returns a list
of the elements that are common to both lists.
'''

def common_elements(lst1, lst2):
	pass

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
common_elements(lst1, lst2) # ["super speed"]

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
common_elements(lst1, lst2) # []

'''
Problem 10: Exposing Superman
Metropolis has a population n, with each citizen assigned an integer id from 1 to n. There's
a rumor that Superman is an ordinary citizen among this group.

If Superman is an ordinary citizen, then:
- Superman trusts nobody.
- Everybody (except for Superman) trusts Superman.
- There is exactly one citizen that satisfies properties 1 and 2.

Write a function expose_superman() that accepts a 2D array trust where trust[i] = [ai, bi]
representing that the person labeled ai trusts the person labeled bi. If a trust relationship
does not exist in the trust array, then such a trust relationship does not exist.

Return the label of Superman if he is hiding amongst the population and can be identified,
or return -1 otherwise.
'''

def expose_superman(trust, n):
	pass

n = 2
trust = [[1, 2]]
expose_superman(trust, n) # 2

n = 3
trust = [[1, 3], [2, 3]]
expose_superman(trust, n) # 3

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
expose_superman(trust, n) # -1