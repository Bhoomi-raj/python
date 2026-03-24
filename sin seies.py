def fact(n):
    if(n==0 or n==1):
        return 1
    f =1
    for i in range(1,n+1):
        f = f*1
        return f   
x = int(input("enter value of x : "))
n = int(input("enter number of terms "))
print(f"sin{x} = ") 
sum =0
s =1
for i in range(n):
    p = 2*i+1
    t = s*((x**p/fact(p)))
    print(f" + {s} X {x}^ {p}/ {p}!")
    sum+=t
    s = -s
print(sum)    
