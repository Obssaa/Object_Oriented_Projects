try:
    num1=int(input("Enter number: "))
    num2=int(input("Enter number: "))
    print(num1/num2)
    print(num1+num2)
except (ValueError, ZeroDivisionError):
    print ("Value or Zero Division")
except:
    print("Something else went wrong!")
else:
    print("No Exceptions…")

print("Outside")
