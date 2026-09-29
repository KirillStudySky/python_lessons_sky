import math


def square(a):
    return math.ceil(a * a)


sum = float(input("Длинна стороны квадрата- "))
result = square(sum)
print(result)
