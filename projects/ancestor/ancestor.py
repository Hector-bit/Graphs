from util import Stack, Queue
"""
Need to find a way to find the oldest ancestor of whatever number we pick,
maybe I can do something similar to the order tickets problem on one of my sprints.
"""
def earliest_ancestor(ancestors, starting_node, valid_ancestor=None):
    #some inputs will have multiple ancestors, pick smaller number when this happens
    if valid_ancestor is None:
        valid_ancestor = set()
    #loop through ancestors
    for i in ancestors:
        print('pair', i)
        #if starting node is in any of the tuples first index then...
        if starting_node != i[0] and starting_node == i[1]: 
            # recurse on the second number
            earliest_ancestor(ancestors, i[0], valid_ancestor)
            print(f'starting node {starting_node} is in this pair {i}, second number in tuple: {i[1]}')
        elif starting_node == i[0] and starting_node != i[1]:
            print('This is a valid ancestor: ', i[0])
            valid_ancestor.add(i[0])
            # if i[1] == starting_node:
            #     return i[0]
    print(valid_ancestor, 'ANCESTORS')
    lowest_numeric = 100
    for j in valid_ancestor:
        if j < lowest_numeric:
            lowest_numeric = j
    print(lowest_numeric, 'lowest')
    return lowest_numeric
