x = int(input("enter no of rows "))
i=1
cnt =0
while i<=x:
    s =1
    while s<=x-i:
        print(" ",end = " ")
        s+=1
    j=1
    while j<=2*i-1:
        print(cnt,end =" ")
        j+=1
        cnt+=1
    print()    
    i+=1        