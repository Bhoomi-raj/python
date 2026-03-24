x = int(input("enter number of rows you want "))
i =1
count =0
for i in range(x+1):
    for j in range(i):
        print(count,end="")
        count+=1
    print()        