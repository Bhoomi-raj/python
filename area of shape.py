def area_rectangle(l,b):
    return l*b
def area_triangle(b,h):
    return l*h
def area_square(s):
    return s**2
shape = input("enter shape ")
if shape== 'rectangle':
    l = int(input("enter length "))
    b = int(input("enter breadth "))
    print("area ",area_rectangle(l,b))
if shape== 'triangle':
    a = int(input("enter length "))
    b = int(input("enter height "))
    print("area ",area_triangle(a,b))    