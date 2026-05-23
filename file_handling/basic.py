file_name = "ayush_result.txt"
#insert
with open(file_name,"a") as fl:
    name = ("bhoomi")
    roll = (1)
    phont = (1234567)
    fl.write(f"{name},{roll},{phont}")
    print("record added succesfull")
#veiw
with open(file_name,"r") as f:
    data = f.readlines()
    if not data:
        print("not data found ")
    else:
        print(data)
        
    