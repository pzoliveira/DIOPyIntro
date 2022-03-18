
if __name__ == '__main__':
    try:
        division = 1 / 1
        nbrlst = [0, 1]
        nbr2 = nbrlst[2]
    except ZeroDivisionError:
        print('There is an error: division by zero')
    except:
        print('Error')
    else:
        print('No problems found!')
    finally:
        print('This piece of code always works!!!')
