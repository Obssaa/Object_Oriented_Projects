def foo():
    try:
        print("Hello")
        raise ValueError
    except:
        print("Problem")
    else:
        print("There ")
    finally:
        print("Bye")
foo()
