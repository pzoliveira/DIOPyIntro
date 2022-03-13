list_int = [3, 201, 5, 190, 78]
list_str = ['one', 'three', 'un', 'trois']
print(list_int)
list_int.sort()
print(list_int)
print(sum(list_int))
for nbr in list_str:
    print(nbr)
list_str[0] = 'uno'
list_str[1] = 'tres'
list_str.reverse()
list_str.append('drei')
list_str.append('eins')
list_str.pop(0)
list_str.remove('un')
tuple_str = tuple(list_str)
print(tuple_str, len(list_int))
