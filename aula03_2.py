a = b = c = d = -100
while a < 0 or a > 10:
    a = int(input('First grade: '))
while b < 0 or b > 10:
    b = int(input('Second grade: '))
while c < 0 or c > 10:
    c = int(input('Third grade: '))
while d < 0 or d > 10:
    d = int(input('Fourth grade: '))
avrg = (a + b + c + d) / 4
print('The average of the grades of the student is: {}'.format(avrg))
if avrg >= 7:
    print('Student approved')
else:
    print('Student not approved')
