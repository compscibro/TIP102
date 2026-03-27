'''
Problem 1: Time Needed to Stream Movies
There are n users in a queue waiting to stream their favorite movies, where the 0th user is
at the front of the queue and the (n - 1)th user is at the back of the queue.

You are given a 0-indexed integer array movies of length n where the number of movies that
the ith user would like to stream is movies[i].

Each user takes exactly 1 second to stream a movie. A user can only stream 1 movie at a time
and has to go back to the end of the queue (which happens instantaneously) in order to stream
more movies. If a user does not have any movies left to stream, they will leave the queue.

Return the time taken for the user at position k (0-indexed) to finish streaming all their
movies.
'''

def time_required_to_stream(movies, k):
	pass

time_required_to_stream([2, 3, 2], 2) # 6
time_required_to_stream([5, 1, 1, 1], 0) # 8

'''
Problem 2: Reverse Watchlist
You are given a list watchlist representing a list of shows sorted by popularity for a
particular user. The user wants to discover new shows they haven't heard of before by
reversing the list to show the least popular shows first.

Using the two-pointer approach, implement a function reverse_watchlist() that reverses the
order of the watchlist in-place. This means that the first show in the given list should
become the last, the second show should become the second to last, and so on. Return the
reversed list.

Do not use list slicing (e.g., watchlist[::-1]) to achieve this.
'''

def reverse_watchlist(watchlist):
	pass

watchlist = ["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"]
reverse_watchlist(watchlist) # ['The Witcher', 'The Crown', 'Stranger Things', 'Breaking Bad']

'''
Problem 3: Remove All Adjacent Duplicate Shows
You are given a string schedule representing the lineup of shows on a streaming platform,
where each character in the string represents a different show. A duplicate removal consists
of choosing two adjacent and equal shows and removing them from the schedule.

We repeatedly make duplicate removals on schedule until no further removals can be made.

Return the final schedule after all such duplicate removals have been made. The answer is
guaranteed to be unique.
'''

def remove_duplicate_shows(schedule):
	pass

remove_duplicate_shows("abbaca") # "ca"
remove_duplicate_shows("azxxzy") # "ay"

'''
Problem 4: Minimum Average of Smallest and Largest View Counts
You manage a collection of view counts for different shows on a streaming platform. You are
given an array view_counts of n integers, where n is even.

You repeat the following procedure n / 2 times:
- Remove the show with the smallest view count, min_view_count, and the show with the largest
  view count, max_view_count, from view_counts.
- Add (min_view_count + max_view_count) / 2 to the list of average view counts average_views.

Return the minimum element in average_views.
'''

def minimum_average_view_count(view_counts):
	pass

minimum_average_view_count([7, 8, 3, 4, 15, 13, 4, 1]) # 5.5
minimum_average_view_count([1, 9, 8, 3, 10, 5]) # 5.5
minimum_average_view_count([1, 2, 3, 7, 8, 9]) # 5.0

'''
Problem 5: Minimum Remaining Watchlist After Removing Movies
You have a watchlist consisting only of uppercase English letters representing movies. Each
movie is represented by a unique letter.

You can apply some operations to this watchlist where, in one operation, you can remove any
occurrence of one of the movie pairs "AB" or "CD" from the watchlist.

Return the minimum possible length of the modified watchlist that you can obtain.

Note that the watchlist concatenates after removing the movie pair and could produce new
"AB" or "CD" pairs.
'''

def min_remaining_watchlist(watchlist):
	pass

min_remaining_watchlist("ABFCACDB") # 2
min_remaining_watchlist("ACBBD") # 5

'''
Problem 6: Apply Operations to Show Ratings
You are given a 0-indexed array ratings of size n consisting of non-negative integers. Each
integer represents the rating of a show in a streaming service.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed),
you will apply the following on the ith element of ratings:

If ratings[i] == ratings[i + 1], then multiply ratings[i] by 2 and set ratings[i + 1] to 0.
Otherwise, you skip this operation.

After performing all the operations, shift all the 0's to the end of the array.

Return the resulting array of ratings.
'''

def apply_rating_operations(ratings):
	pass

apply_rating_operations([1, 2, 2, 1, 1, 0]) # [1, 4, 2, 0, 0, 0]
apply_rating_operations([0, 1]) # [1, 0]

'''
Problem 7: Lexicographically Smallest Watchlist
You are managing a watchlist for a streaming service, represented by a string watchlist
consisting of lowercase English letters, where each letter represents a different show.

You are allowed to perform operations on this watchlist. In one operation, you can replace a
show in watchlist with another show (i.e., another lowercase English letter).

Your task is to make the watchlist a palindrome with the minimum number of operations
possible. If there are multiple palindromes that can be made using the minimum number of
operations, make the lexicographically smallest one.

A string a is lexicographically smaller than a string b (of the same length) if in the first
position where a and b differ, string a has a letter that appears earlier in the alphabet
than the corresponding letter in b.

Return the resulting watchlist string.

Implement the following pseudocode:
1. Convert the watchlist string to a list.
2. Initialize two pointers:
   * Left Pointer: Start at the beginning of the list (index 0).
   * Right Pointer: Start at the end of the list (last index).
3. While the left pointer is less than the right pointer:
   a. Compare the characters at the left and right pointers.
   b. If the characters are different:
      * Replace the character that is alphabetically later (greater) with the one that is
        earlier (smaller) to make the string lexicographically smaller.
   c. Move the left pointer one step to the right.
   d. Move the right pointer one step to the left.
4. Convert the list back to a string.
5. Return the resulting string.
'''

def make_smallest_watchlist(watchlist):
	pass

make_smallest_watchlist("egcfe") # "efcfe"
make_smallest_watchlist("abcd") # "abba"
make_smallest_watchlist("seven") # "neven"
