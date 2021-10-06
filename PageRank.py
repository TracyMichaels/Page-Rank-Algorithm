#!/usr/bin/env python
# coding: utf-8

# # Tracy Michaels
# 
# ## CSC 4740 Data Mining - Assignment 3
# ***
# ### Implementing a PageRank Algorithm
# ***

import collections
import pprint as pp

# worker method
def getContributions(d):
    for key in d:
        for i in d[key][0]:
            yield(i, d[key][1]/len(d[key][0]))

# import file as list
f = open("01AdjacencyList.txt", "r")
# each line in file to a list
adj_ls = f.read().splitlines()
f.close()

print("Input list: ")
pp.pprint(adj_ls)

# each list value to its own list
adj_ls = [i.split() for i in adj_ls]
# print(adj_ls) #debug

# parse ints
adj_ls = [[int(j) for j in i] for i in adj_ls]
# print(adj_ls) #debug

# separate node from paths
adj_ls = [[i[0], i[1:]] for i in adj_ls]
# print(adj_ls) #debug

num_nodes = len(adj_ls)
print(f'Number of Nodes: {num_nodes}')

# initalize values
init_vals = [(i[0], 1/num_nodes) for i in adj_ls]
# print(init_vals) #debug

#convert each to dict
adj_dict = dict(adj_ls)
val_dict = dict(init_vals)

# 30 iterations of power iteration method
for i in range(30):
    print(f'iteration: {i}')
    # join init values with list
    join_dict = dict((k, (adj_dict[k], val_dict[k])) for k in adj_dict)
#     pp.pprint(join_dict) #debug

    # contributions
    cont_ls = list(getContributions(join_dict))
#     pp.pprint(cont_ls) #debug

    # consolidate by key into dict
    cons_dict = {k:0 for k,v in cont_ls}
    for k,v in cont_ls:
        cons_dict[k] += v
#     pp.pprint(cons_dict) #debug

    # rank values
    for k in cons_dict:
        val_dict[k] = (cons_dict[k]*0.85)+(.15/num_nodes)
    pp.pprint(val_dict)
    
print()
print("final result: ")

pp.pprint(val_dict)


