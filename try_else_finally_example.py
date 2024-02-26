num1 = 0
def readNum():
    res = int(input("Enter a number"))
    return res
try:
    num1 = readNum()
except ValueError:
    print("Wrong Input")
else:
    print("No problems")
finally:
    print("Let's move on")
print("Outside")

