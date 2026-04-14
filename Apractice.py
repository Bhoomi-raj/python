def rep(s,a,b):
    new_str = ""
    for i in range(len(s)):
        if s[i]==a:
            new_str+=b
        else:
            new_str+=s[i]
    return new_str            


s = input("enter string ")
a = input("enter char replace ")
b = input("enter char to replace with ")
print("original string ",s)
print("replaced string ",rep(s,a,b))            