'''a = int(input("enter value of n "))
if(a%2==0):
    print("it is not a prime number")
elif(a%2!=0):
    print("it is a prime number ")
else:
    print("valid number") '''

time = int(input("enter time "))
if(time>1):
    if(time<12):
        print("good morning")
elif(time>=12):
    if(time < 16):
        print("good afternoon")
else :
    print("good night")                       