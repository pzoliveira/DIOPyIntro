from aula07_2 import Calculator
from aula08_2 import lttrscntr, totaloflttrs

if __name__ == '__main__':
    calc = Calculator(10, 2)
    print(calc.sums())
    numbers = ['one', 'two', 'three']
    lttrspwlst = lttrscntr(numbers)
    totalLttrs = totaloflttrs(numbers)
    print('The list of the total letters per word is {}'.format(lttrspwlst))
    print('The total of letters is {}'.format(totalLttrs))
