def palich(s):
    s = s.lower()
    if(s==s[::-1]):
        return True
    return False
x = input("enter string ")
print(palich(x))