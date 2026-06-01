a = 0
b = 1

x = int(input("Enter value: "))

for i in range(x):
    print(a, end=" ")
    s = a + b
    a = b
    b = s