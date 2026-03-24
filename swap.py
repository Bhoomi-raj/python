#swap
l1 =[]
n = int(input("enter number of terms "))
for i in range(n):
    x = int(input("enter number of terms "))
    l1.append(x)
    print(l1)
print("enter terms to swap ")
n1 = int(input("enter value of n1 "))
n2 = int(input("enter value of n2 "))
e1=e2=0
for i in range(n):
    if(n1 in l1 and n2 in l1):
        if(l1[i]==n1):
            e1 =i
        if(l1[i] == n2):
            e2 = i
l1[e1],l1[e2] = l1[e2],l1[e1]
print(l1)            
