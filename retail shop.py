ch = 'y'
bill =0
while(ch=='y'):
    a = input("enter name of item ")
    cost = int(input("enter price of that item "))
    bill+=cost 
    ch = input('do you want to add more item ')

print("total bill","-> ",bill)   