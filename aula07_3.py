class Calculator:
    def sums(self, avalue, bvalue):
        return avalue + bvalue

    def subtr(self, avalue, bvalue):
        return avalue - bvalue

    def mult(self, avalue, bvalue):
        return avalue * bvalue

    def div(self, avalue, bvalue):
        return avalue / bvalue


calc = Calculator()
print(calc.sums(10, 2))
print(calc.subtr(10, 2))
print(calc.mult(10, 2))
print(calc.div(10, 2))
