'''
Write a function to reverse a singly linked list. 
The function should take the head of a linked list as input 
and return the new head of the reversed linked list.

U:
    input: 1->2->3 (singly LL)
    output: 3->2->1 (singly LL)

M:
    Singly LinkedList
    Handle empty node
    Return the node if there is only one
'''

def reverse_list(head):
    if head is None:
        return None
    
    