# x =2
# y =11
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i*j :4}",end ="")
#     print()    


# x = int(input("enter income "))
# if(x<=10000):
#     print("no tax")
# elif(x > 10000 and x < 20000):
#     tax = x*10/100
#     print(tax)
# else:
#     tax = 20*x/100
#     print(tax)


# x = int(input("enter number "))
# ans =0
# while(x!=0):
#     digit = x%10
#     ans = ans*10 + digit
#     x = x//10
# print(ans)    




l1 = []
l2 = []
n = int(input("enter size for first list "))
m = int(input("enter size of second list "))
for i in range(n):
    x = int(input("enter value for list1 "))
    l1.append(x)
for i in range(m):
    y = int(input("enter value for list2 "))
    l2.append(y)  
print("l1 : ",l1,end = "")
print("l2 : ",l2,end = "")
l3 =[]
size = n+m
for i in range(n):
    if(l1[i]%2==0):
        l3.append(l1[i])
for i in range(m):
        if(l2[i]%2!=0):
         l3.append(l2[i])  
print("l3" , l3)       