# Personal Solutions
"""
Problem 1: Reverse Sentence

    Write a function reverse_sentence() that takes in a string sentence and 
    returns the sentence with the order of the words reversed. The sentence 
    will contain only alphabetic characters and spaces to separate the words.
    If there is only one word in the sentence, the function should return 
    the original string.

Example Usage:

    sentence = "tubby little cubby all stuffed with fluff"
    reverse_sentence(sentence)

    sentence = "Pooh"
    reverse_sentence(sentence)

Example Output:

    "fluff with stuffed all cubby little tubby"
    "Pooh"

Note:
    Reverse the order of words.
    Time complexity: O(n)
    Space complexity: O(n)
"""
def reverse_sentence(sentence):

    # convert string into a list of splitted words: O(n)
    words = sentence.split()

    # reverse the list: O(n)
    words.reverse()

    # covert list back into a string with a space: O(n)
    return " ".join(words)

# tests
multi_words_sentence = "tubby little cubby all stuffed with fluff"
test = reverse_sentence(multi_words_sentence)
print(test)

one_word_sentence = "Pooh"
test = reverse_sentence(one_word_sentence)
print(test)

# challenge: what if you cannot use .split()?





"""
Problem 2: Goldilocks Number

    In the extended universe of fictional bears, Goldilocks finds an enticing 
    list of numbers in the Three Bears' house. She doesn't want to take a number 
    that's too high or too low - she wants a number that's just right. Write a 
    function goldilocks_approved() that takes in the list of distinct positive 
    integers nums and returns any number from the list that is neither the minimum
    nor the maximum value in the array, or -1 if there is no such number.

    Return the selected integer.

Example Usage:

    nums = [3, 2, 1, 4]
    goldilocks_approved(nums)

    nums = [1, 2]
    goldilocks_approved(nums)

    nums = [2, 1, 3]
    goldilocks_approved(nums)

Example Output:

    3
    -1
    2

Note:
    Time complexity: O(n)
    Space complexity: O(1)
"""
def goldilocks_approved(nums):
    # no such number check: O(1)
    if len(nums) < 3:
        return -1

    # find the max and min number: O(n), O(n)
    max_num = max(nums)
    min_num = min(nums)

    # find the integer that is not min and max: O(n)
    for i in nums:
        if i != min_num and i != max_num:
            return i
    return -1

# tests
nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))

# challenge: What is the smallest possible input size where a second smallest element exists?





"""
Problem 3: Delete Minimum

    Pooh is eating all of his hunny jars in order of smallest to largest. 
    Given a list of integers hunny_jar_sizes, write a function 
    delete_minimum_elements() that continuously removes the minimum element 
    until the list is empty. Return a new list of the elements of 
    hunny_jar_sizes in the order in which they were removed.

Example Usage:

    hunny_jar_sizes = [5, 3, 2, 4, 1]
    delete_minimum_elements(hunny_jar_sizes)

    hunny_jar_sizes = [5, 2, 1, 8, 2]
    delete_minimum_elements(hunny_jar_sizes)

Example Output:

    [1, 2, 3, 4, 5]
    [1, 2, 2, 5, 8]

Notes:
    Time complexity: O(n^2)
    Space complexity: O(n)
"""
def delete_minimum_elements(hunny_jar_sizes):
    # create an empty result list
    result = []
    # use while loop
    while len(hunny_jar_sizes) != 0:

        # record min: O(n)
        min_val = min(hunny_jar_sizes)

        # add the min to the new list: amortized O(1)
        result.append(min_val)
    
        # remove the min: O(n)
        hunny_jar_sizes.remove(min_val)

    # return the new list
    return result

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))

# challenge: how to optimize it to be O(n log n) instead of O(n^2)? 
# solution: just use sorted(hunny_jar_sizes)