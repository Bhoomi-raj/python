a = int(input("enter vale of a "))
b = int(input("enter value of b "))
choice = input("enter operator ")
match choice :
    case "+" : print("addition ",a+b)
    case "-" : print("subtraction ",a-b)
    case "*" : print("multiplication ",a*b)
    case "/" : 
        if(b!=0) :
            print("division ",a/b)
        else :
            print("canot divide by zero")
    case _:
        print("enter valid operator")