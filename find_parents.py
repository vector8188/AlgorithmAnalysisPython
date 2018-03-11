            
# 1   2   4
#  \ /   / \
#   3   5   8
#    \ / \   \
#     6   7   9

# Write a function that takes this data as input and returns two collections: one containing all individuals with zero known parents, and one containing all individuals with exactly one known parent.

# Sample output (pseudocode):
# [
#   [1, 2, 4],   // Individuals with zero parents
#   [5, 7, 8, 9] // Individuals with exactly one parent
# ]

parent_child_pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (8, 9)
]

# children_parent = {
#     3:[1,2], 6:[3,5], 7:[5], 5:[4], 8:[4], 9:[8]
# }

def f(parent_child_pairs):
    children_parent = {}
    individuals_exactly_one = []
    individuals_zero = [] 
    for items in parent_child_pairs:
        children_parent[items[1]] = []
    for items in parent_child_pairs:
        children_parent[items[1]].append(items[0])
        
    for k,v in children_parent.items():
        if len(v) == 1:
            individuals_exactly_one.append(k)
        if len(v)>1:
            if v[1] not in  children_parent.keys():
                individuals_zero.append(v[1])
        if v[0] not in  children_parent.keys():
            individuals_zero.append(v[0])
            
    return (individuals_exactly_one, set(individuals_zero))
    
print (f(parent_child_pairs))
