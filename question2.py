a , b= 2,3
print(f"before : {a},{b}")
a,b =b,a
print(f"after :{a},{b}")
#circular rotation
a,b,c = 10,20,30;
print(f"before : {a},{b},{c}")
a,b,c = b,c,a;
print(f"after : {a},{b},{c}")