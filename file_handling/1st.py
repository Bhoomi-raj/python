# f = open("char cnt.py")
# print(f.read())

# using w will overwrite the content
#using a will add in the existing content
with open("area of shape.py") as f:
    f.write("finding area of shape")
with open("area of shape.py") as f:
    print(f.read())    