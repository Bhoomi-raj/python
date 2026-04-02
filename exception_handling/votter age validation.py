try:
    age =int(input("enter age "))
    if age<18:
        print("eligible to vote")
except ValueError:
    print("not eligible to vote ")        