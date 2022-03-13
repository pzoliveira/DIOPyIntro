nbr = int(input('Enter the number: '))

cnt = 0

for i in range(2, nbr+1):
    if nbr % i == 0:
        cnt += 1

if cnt == 1:
    print('Prime')
else:
    print('Not prime')
