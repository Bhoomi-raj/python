'''x1 = int(input("enter value of x1 "))
x2 = int(input("enter value of x2 "))
y1 = int(input("enter value of y1 "))
y2 = int(input("enter value of y2 "))
dist = float((x2-x1)**2 + (y2-y1)**2)**0.5
print("dist between two point ",dist,sep="->")
'''


l1 = []
x = int(input("enter number of terms "))
for i in range(x):
    n = int(input("enter terms "))
    l1.append(n)
    print(l1)
print("enter two points for dist ")
x1 = int(input("enter value of x1 "))
x2 = int(input("enter value of x2 "))
y1 = int(input("enter value of y1 "))
y2 = int(input("enter value of y2 "))
if(x1 in l1 and x2 in l1 and y1 in l1 and y2 in l1):
    dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
    print("dist between two two point ",dist,sep ="-> ")
else:
    print("value is not present in list ")    