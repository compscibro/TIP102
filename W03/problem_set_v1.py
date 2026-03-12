# Problem 1: Manage Performance Stage Changes

def manage_stage_changes(changes): # strings (each string list a change action)
    # empty list for the answer
    performing = []
    not_performing = []

    # loop changes
    for s in changes:

        temp = s.split() 
        
        # edge case:
        # if stack.isEmpty()
        if len(changes) == 0:
            return []
        # 2 stacks (one is for scheduled and the other one is for canceled)
        # if "Schedule X", add X to stack 1
        elif temp[0] == "Schedule":
            performing.append(temp[1])
        # if "Cancel", stack 1 pop(), add the popped element to stack 2
        elif s == "Cancel":
            #not_performing.append(s)
            temp = performing.pop()
            not_performing.append(temp)
        # if "Reschedule", make a varaiable to store the value -> variable = stack 2 pop() -> add the element back to stack 1
        else:
            performing.append(not_performing[-1])
    return performing
    


# tests
# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"])) # ["A", "C", "B", "D"]
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) # []
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) # ["Z"]


# Problem 2: Queue of Performance Requests
def process_performance_requests(requests):
    # sort the requests by number 5 -> 1
    sorted_request = sorted(requests, reverse = True)
    # accoring to priority, add String(value) to queue
    # return queue
    return sorted_request
    



# tests
print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

# ['Music', 'Dance', 'Drama']
# ['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']
# ['Keynote Speech', 'Panel Discussion', 'Film Screening', 'Workshop', 'Art Exhibition']