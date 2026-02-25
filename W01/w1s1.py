print("\nWeek 1 Session 1\n")

# https://prod.liveshare.vsengsaas.visualstudio.com/join?D5D1DEADB6A599793326AC10BAE47FB4563F


# Problem 1: Reverse Sentence
def reverse_sentence(sentence):
    # initialize an empty string
    # left, right pointer for either ends
    # swap the characters at either ends in a while loop
    # bring pointers in during each iteration until they cross
    # return the reversed string
    left, right = 0, len(sentence) - 1
    sentence_list = list(sentence) # O(n)
    
    while left < right: # O(n/2)
        sentence_list[right], sentence_list[left] = sentence_list[left], sentence_list[right]
        left += 1
        right -= 1
    
    return "".join(sentence_list) # O(n)

# print(reverse_sentence('hello'))

# O(n)

# olleh


# Problem 2: Goldilocks Number
# for loop_variable in nums:
def goldilocks_approved(nums):

    if nums == []:
        return -1
        
    
    max_num = max(nums) # O(n)
    min_num = min(nums) # O(n)

    for i in nums: # O(1)
        if (i != max_num or i != min_num): # early termination condition
            return i

    return -1

# print(goldilocks_approved([3, 2, 1, 4]))

# O(n)
# O(1)

# Problem 3: Delete Minimum
def delete_minimum_elements(hunny_jar_sizes):
    # hint: while loop

    # record min

    # remove the min

    # add the min to the new list

    # return the new list

