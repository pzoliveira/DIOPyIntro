a = int(input('First: '))
b = int(input('Second: '))
c = int(input('Third: '))

if a > b and a > c:
    rslt = a
elif b > a and b > c:
    rslt = b
else:
    rslt = c
print('The greatest value is {}'.format(rslt))
print('End of the program')
