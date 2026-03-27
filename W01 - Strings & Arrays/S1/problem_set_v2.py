'''
Problem 1: Batman
Write a function batman() that prints the string "I am vengeance. I am the night. I am Batman!".
'''

def batman():
	pass

batman() # I am vengeance. I am the night. I am Batman!

'''
Problem 2: Mad Libs
Write a function madlib() that accepts one parameter, a string verb. The function should print
the sentence: "I have one power. I never <verb>. - Batman".
'''

def madlib(verb):
	pass

verb = "give up"
madlib(verb) # "I have one power. I never give up. - Batman"

verb = "nap"
madlib(verb) # "I have one power. I never nap. - Batman"

'''
Problem 3: Trilogy
Write a function trilogy() that accepts an integer year and prints the title of the Batman
trilogy movie released that year as outlined below.

Year        Movie Title
2005        "Batman Begins"
2008        "The Dark Knight"
2012        "The Dark Knight Rises"

If the given year does not match one of the years in the table above, print
"Christopher Nolan did not release a Batman movie in <year>."
'''

def trilogy(year):
	pass

year = 2008
trilogy(year) # "The Dark Knight"

year = 1998
trilogy(year) # "Christopher Nolan did not release a Batman movie in 1998."

'''
Problem 4: Last
Implement a function get_last() that accepts a list of items items and returns the last item
in the list. If the list is empty, return None.
'''

def get_last(items):
	pass

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items) # "black adam"

items = []
get_last(items) # None

'''
Problem 5: Concatenate
Write a function concatenate() that takes in a list of strings words and returns a string
concatenated that concatenates all elements in words.
'''

def concatenate(words):
	pass

words = ["vengeance", "darkness", "batman"]
concatenate(words) # "vengeancedarknessbatman"

words = []
concatenate(words) # ""

'''
Problem 6: Squared
Write a function squared() that accepts a list of integers numbers as a parameter and squares
each item in the list. Return the squared list.
'''

def squared(numbers):
	pass

numbers = [1, 2, 3]
squared(numbers) # [1, 4, 9]

'''
Problem 7: NaNaNa Batman!
Write a function nanana_batman() that accepts an integer x and prints the string
"nanana batman!" where "na" is repeated x times. Do not use the * operator.
'''

def nanana_batman(x):
	pass

x = 6
nanana_batman(x) # "nananananana batman!"

x = 0
nanana_batman(x) # "batman!"

'''
Problem 8: Find the Villain
Write a function find_villain() that accepts a list crowd and a value villain as parameters
and returns a list of all indices where the villain is found hiding in the crowd.
'''

def find_villain(crowd, villain):
	pass

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain) # [1, 4, 6]

'''
Problem 9: Odd
Write a function get_odds() that takes in a list of integers nums and returns a new list
containing all the odd numbers in nums.
'''

def get_odds(nums):
	pass

nums = [1, 2, 3, 4]
get_odds(nums) # [1, 3]

nums = [2, 4, 6, 8]
get_odds(nums) # []

'''
Problem 10: Up and Down
Write a function up_and_down() that accepts a list of integers lst as a parameter. The function
should return the number of odd numbers minus the number of even numbers in the list.
'''

def up_and_down(lst):
	pass

lst = [1, 2, 3]
up_and_down(lst) # 1

lst = [1, 3, 5]
up_and_down(lst) # 3

lst = [2, 4, 10, 2]
up_and_down(lst) # -4

'''
Problem 11: Running Sum
Write a function running_sum() that accepts a list of integers superhero_stats representing
the number of crimes Batman has stopped each month in Gotham City. The function should modify
the list to return the running sum such that superhero_stats[i] = sum(superhero_stats[0]...
superhero_stats[i]). You must modify the list in place; you may not create any new lists as
part of your solution.
'''

def running_sum(superhero_stats):
	pass

superhero_stats = [1, 2, 3, 4]
running_sum(superhero_stats) # [1, 3, 6, 10]

superhero_stats = [1, 1, 1, 1, 1]
running_sum(superhero_stats) # [1, 2, 3, 4, 5]

superhero_stats = [3, 1, 2, 10, 1]
running_sum(superhero_stats) # [3, 4, 6, 16, 17]

'''
Problem 12: Shuffle
Write a function shuffle() that accepts a list cards of 2n elements in the form
[x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].
'''

def shuffle(cards):
	pass

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards) # ['Joker', 3, 'Queen', 'Ace', 2, 7]

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards) # [9, 'Joker', 2, 3, 3, 2, 'Joker', 9]

cards = [10, 10, 2, 2]
shuffle(cards) # [10, 2, 10, 2]
