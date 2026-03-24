students = []

while True:
    ch = input("\n1 Add  2 View  3 Exit : ")

    if ch == '1':
        roll = int(input("Roll: "))
        name = input("Name: ")
        students.append((roll, name))   

    elif ch == '2':
        for s in students:
            print(s)

    elif ch == '3':
        break
