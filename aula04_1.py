nbr = int(input('Enter the number: '))

for x in range(2, nbr+1):
    cnt = 0
    for i in range(2, x+1):
        if x % i == 0:
            cnt += 1
    if cnt == 1:
        print(x)
