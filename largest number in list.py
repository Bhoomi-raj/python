l1 = []
x = int(input("enter len of list "))
for i in range(x):
    a = int(input("enter ele "))
    l1.append(a)
print("list ",l1) 
maxi = l1[0]
for i in l1:
    if i > maxi:
        maxi = i

print("maximum ele ",maxi)           