try:
    age = int(input("Enter your age: "))
    if (age<0) or (age>120):
        raise ValueError
    else:
        print("Thank you")
except ValueError:
    print("Age given is Wrong")
