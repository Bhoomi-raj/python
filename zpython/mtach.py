'''x = int(input("enter value "))
match x:
    case 0 : 
        if(x!=7):
          print("x is not 7")
    case 1 :
      if(x!=9):
         print("x is not 9")
    case _  :
         print("enter valid number")'''
x = input("enter operator ")
a = int(input("enter value of a "))
b = int(input("enter value of b "))
match x:
    case '+':
        print((a+b),"addition value ")
    case '-':
        print((a-b)," subtraction value ")
    case '*':
        print((a*b) ,"multiplication value ")
    case '/':
        print((a/b) ,"division value ")
    case _:
        print("enter valid operator ")
                
           