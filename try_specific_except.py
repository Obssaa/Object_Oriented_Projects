try:
    num1=int(input("Enter number: "))
    num2=int(input("Enter number: "))
    print(num1/num2)
    print(num1+num2)
except ValueError:
    print("You are required to enter integers.")
except ZeroDivisionError:
    print("Division by zero is not allowed")
except:
    print("Something else went wrong!")
