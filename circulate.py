x = int(input("enter number of time want to circulate "))
cnt =0
l1 = []
l = int(input("enter len of list "))
for i in range(l):
    a = int(input("enter ele "))
    l1.append(a)
print("original list ",l1)
    
while(cnt<x):
    first = l1.pop(0)
    l1.append(first)
    cnt+=1
print("list after x rotation " , l1)    