# x = int(input("enter number of rows you want "))
# i =1
# count =1
# while(i<=x):
#     j=1
#     while(j<=i):
#         print(count,end =" ")
#         count = count+1
#         j = j+1
#     print()
#     i = i+1
# x = int(input("enter number of rows "))
# i =1
# count=0
# while(i<=x):
#     space =1
#     while(space <= x-i):
#         print(" ",end = "")
#         space+=1
#     start =1 
      
#     while(start<= 2*i-1):
#         print(count,end="")
#         count+=1
#         start+=1
#     print()
#     i+=1        
#-----------------------------------------------------
x = int(input("enter the value of n "))
i =1
count =1
while(i<x):
    space =1
    while(space<=x-i):
        print(" ",end = " ")
        space+=1
    start =1
    while(start<=2*i-1):
        print(count,end = " ")
        count+=1
        start+=1
    print()
    i+=1        