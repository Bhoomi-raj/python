# def gmean(a ,b):
#     mean = (a*b)/(a+b)
#     print(mean)
# def isgreater(a,b):
#     if(a>b):
#         print("first element is greater ")
#     else:
#         print("second element is grester or equal ")        
# a = int(input("enter the value of a "))
# b = int(input("enter the value of b "))
# isgreater(a,b)
# gmean(a,b) 
# 
# --------------default argument----------------   
# def average(a =8,b=3):
#     av = (a+b)/2
#     print("average value of a and b : ",av,sep='->')
# average(b=2)
#----------------------average--------------------
# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum+i;
#     print("averge value og given number of n terms is ",sum/len(numbers))
# average(2,7,4,5,9)    
def fact(n):
    if(n==0 or n==1):
        return 1
    f =1
    for i in range(1,n+1):
        f = f*i;
    return f;  
x = int(input("enter value of n "))
fact(x);
print(fact(x))    
