def isIntEven(nbr):
    rslt = False
    if nbr % 2 == 0:
        rslt = True
    return rslt

if __name__ == '__main__':
    a = int(input('Enter number: '))
    if(isIntEven(a)):
        print('Even')
    else:
        print('Not even')
