class Calculator:
    def __init__(self, num1, num2):
        self.avalue = num1
        self.bvalue = num2

    def sums(self):
        return self.avalue + self.bvalue

    def subtr(self):
        return self.avalue - self.bvalue

    def mult(self):
        return self.avalue * self.bvalue

    def div(self):
        return self.avalue / self.bvalue


calc = Calculator(10, 2)
print('a value = {}\nb value = {}'.format(calc.avalue, calc.bvalue))
print(calc.sums())
print(calc.subtr())
print(calc.mult())
print(calc.div())
