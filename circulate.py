x = int(input("enter number of circulation you want "))
cnt =0
l1 =[]
n = int(input("enter number of terms "))
for i in range(n):
    t = int(input("enter terms "))
    l1.append(t)
print("original list ",l1,sep = "-> ")
while(cnt<x):
    first = l1.pop(0)
    l1.append(first)
    cnt+=1
print("after x rotation list ",l1,sep ="-> ")    
