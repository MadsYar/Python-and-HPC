import numpy as np

def listsum(lst):
    return sum(lst)

#print(list_sum([1, 2, 3, 4]))

def deduplicate(lst):
    return list(set(lst))

#print(deduplicate([1, 2, 3, 3, 2, 2, 4]))

def sorttuples(lst):
    return sorted(lst, key=lambda x: x[-1])

#print(sorttuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

def squarecubes(lst):
    squares = [x**2 for x in lst]
    cubes = [x**3 for x in lst]
    return (squares, cubes)

print(squarecubes([1, 2, 3, 4])) 

