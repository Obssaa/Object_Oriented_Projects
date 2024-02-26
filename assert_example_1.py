# Square a negative number
def squareNeg(x):
    assert x < 0 #we are watching for x being less than zero. If not, an assertion error will happen
    return x ** 2
try:
    print(squareNeg(3))
except AssertionError:
    print("We need a negative value.")
