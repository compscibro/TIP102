# stacks
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop()) # 3

# queues
from collections import deque

q = deque()
q.append(1)
q.append(2)

removeElement1 = q.popleft() # 1
print(removeElement1)

removeElement2 = q.pop() # 2
print(removeElement2)

# demo
def is_balanced_parentheses(s):
    # initialize an empty stack
    stack = []
    # loop through the characters of the string
        # if its opening, push it on the stacks
        # if its closing, )
            # if stack is empty, return false
            # pop from the stack
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop() 
    # return true if the stack is empty
    return len(stack) == 0

print(is_balanced_parentheses("()()"))

