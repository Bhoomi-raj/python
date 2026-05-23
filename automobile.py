components = {
    "brake,lights,engine,horn,mirror"
}
print("components ",components)

status = {
    "brake" : "working"
    ,"lights" : "working"
    ,"engine" : "not working"
    ,"horn" : "working"
    ,"mirror" : "working"
}
for parts in status:
    print(parts , "is ", status[parts])
for parts in status:
    if(status[parts]=="not working"):
        print("damaged part ",parts)    