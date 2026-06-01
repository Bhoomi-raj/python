def add(*args):
    return sum(args)
def sub(*args):
    res = args[0]
    for i in args[1:]:
        res-=i
    return res
    
def multiplication(*args):
    res = args[0]
    for i in args[1:]:
        res = res*i
    return res
numbers = list(map(int,input("enter numbers ").split()))    
op = input("enter operation ")
if op=='+':
    print("additon ",add(*numbers))
elif op=='-':
    print("subtraction ",sub(*numbers))
elif op=='*':
    print("multiplication ",multiplication(*numbers))
