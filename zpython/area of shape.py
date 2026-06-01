def area_rectangle(l,b):
    return l*b
def area_cir(r):
    pie = 3.14
    return pie*r*r
def area_sqr(s):
    return s*s


while(True):
    x = int(input("press 1 for rectangle , press 2 for circle, press 3 for sqr "))
    if(x==1):
        l = int(input("enter length "))
        b = int(input("enter breadth "))
        print("rect ",area_rectangle(l,b))
    elif(x==2):
        r = int(input("enter radius "))
        print("circle ",area_cir(r))
    elif(x==3):
        s = int(input("enter side "))
        print("sqr ",area_sqr(s))
    else:
        break;            
