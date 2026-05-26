try:
    x =int(input("enter numerator "))
    y = int(input("enter denomenator "))
    print(x/y)
except ZeroDivisionError:
    print("number cannot be divided by zero")
