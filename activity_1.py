try:
    num1 = int(input("Enter number: ")) # we could get a non-int/string
    num2 = int(input("Enter number: ")) # we could get a non-int/string
    print(num1/num2) # we get division by zero
    print(num1+num2)
    print("Hello World 1")
except:
    print("An error has happened")

print("Hello World 2")

