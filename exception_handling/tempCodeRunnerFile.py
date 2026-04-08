try:
    a = int(input("enter marks "))
    if a<0 or a>100:
        print("invalid marks")
    else:
        print("valid marks")
except ValueError:
    print("invalid marks")
