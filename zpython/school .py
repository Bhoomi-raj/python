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

stud =  {}
id = set()
while True:
    ch = int(input("press 1 to add , press 2 to update , pree 3 to veiw ,press 4 to exist "))
    if ch==1:
        sid = int(input("enter stud id "))
        if sid in id:
            print("stude id already exist ")
        else:
            name = input("enter name ")
            phone = int(input("enter phone number "))

            stud[sid] = [name,phone]     
            id.add(sid)
    elif ch==2:
        sid = int(input("enter studen id "))
        if sid in id:
            name = input("enter new name ")
            phone = int(input("enter new phone number "))

            stud[sid] = [name,phone]
            print("data updates succesfully")
        else:
           print("id not found ")
    elif ch==3:
        for sid in stud:
            print("id","name",sid,stud[sid][0],"phone number ",stud[sid][1])

        
    else:
        break       