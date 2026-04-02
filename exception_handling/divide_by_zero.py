try:
    a = int(input("enter number "))
    b = int(input("enter number "))
    res = a/b
    print("result ",res)
except ZeroDivisionError:
    print("error cnnot divide by zero ")
