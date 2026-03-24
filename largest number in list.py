def maxele(l1):
    ans = l1[0]  
    for i in range(len(l1)):
        t = l1[i]
        ans = max(ans,t)
    return ans

l1 = []
x = int(input("enter size of list "))
for i in range(x):
    a = int(input("enter value "))
    l1.append(a)
maxele(l1)
print("max element in l1 is  ",maxele(l1))    
