setone = {1, 3, 5, 7}
settwo = {7, 9, 11}
setu = setone.union(settwo)
print('Union: {}'.format(setu))
seti = setone.intersection(settwo)
print('Intersection: {}'.format(seti))
setd12 = setone.difference(settwo)
setd21 = settwo.difference(setone)
print('Difference 1-2: {}\nDifference 2-1: {}'.format(setd12, setd21))
setsd = setone.symmetric_difference(settwo)
print('Symmetrical difference: {}'.format(setsd))
