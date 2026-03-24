def cnt(s,charchter):
    cn =0
    for i in range(0,len(s)):
        if(s[i]==charchter):
            cn+=1
    return cn
x = input("enter string ")
y = input("enter charachter ")
print(cnt(x,y))        