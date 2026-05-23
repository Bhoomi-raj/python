file_name = "ayush_result.txt"
with open(file_name,'w') as df:
    name = "ayush"
    roll = 5
    df.write(f"{name},{roll}")
    print("data is added successfully ")

with open(file_name,'r') as df:
    data = df.read()
    word = data.split()
    print(word)

with open(file_name,"r") as f:
    content = f.readlines()
    content = [ line.replace("ayush","bhoomi") for line in content]
with open(file_name,"w") as f:
    f.writelines(content)    