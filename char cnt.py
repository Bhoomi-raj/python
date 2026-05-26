def cnt(s,a):
    count =0
    for i in s:
        if(i==a):
            count+=1
    return count
s = input("enter string ")
a = input("enter char ")
print("char count is ",cnt(s,a))
        
    