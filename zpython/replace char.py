def rep(sen,c1,c2):
    new_sen = sen.replace(c1,c2)
    return new_sen
x = input("enter string ")
y = input("enter first char ")
z = input("enter second char ")
print(rep(x,y,z))