# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0

class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def substract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return '0으로 나눌 수 없습니다.'

calc = Calculator()
print(calc.add(1,2))
print(calc.substract(2,1))
print(calc.multiply(3,4))
print(calc.divide(4,0))