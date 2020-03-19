
from graph import Graph
"""
Need to find a way to find the oldest ancestor of whatever number we pick,
maybe I can do something similar to the order tickets problem on one of my sprints.
"""
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for i in ancestors:
        if i[0] not in graph.vertices:
            graph.add_vertex(i[0])
        if i[1] not in graph.vertices:
            graph.add_vertex(i[1])

    for i in ancestors:
        graph.add_edge(i[1], i[0])

    path = graph.bft(starting_node)
    oldest = path[-1]

    if starting_node == oldest:
        return -1
    else:
        return oldest
    # #some inputs will have multiple ancestors, pick smaller number when this happens
    # if valid_ancestor is None:
    #     valid_ancestor = set()
    # #loop through ancestors
    # for i in ancestors:
    #     print('pair', i)
    #     #if starting node is in any of the tuples first index then...
    #     if starting_node != i[0] and starting_node == i[1]: 
    #         # recurse on the second number
    #         earliest_ancestor(ancestors, i[0], valid_ancestor)
    #         print(f'starting node {starting_node} is in this pair {i}, second number in tuple: {i[1]}')
    #     elif starting_node == i[0] and starting_node != i[1]:
    #         print('This is a valid ancestor: ', i[0])
    #         valid_ancestor.add(i[0])
    #         # if i[1] == starting_node:
    #         #     return i[0]
    # print(valid_ancestor, 'ANCESTORS')
    # lowest_numeric = 100
    # for j in valid_ancestor:
    #     if j < lowest_numeric:
    #         lowest_numeric = j
    # print(lowest_numeric, 'lowest')
    # return lowest_numeric
