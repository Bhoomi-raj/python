# # class dog:
# #     sound = "bark"
# # animal = dog() 
# # print(dog.sound)      
# class human:


# ##### class instance 
#     species = "monkey"
#     def __init__(self,name,parent,colour):
#         #### instance variable
#         self.name=name
#         self.parent = parent
#         self.colour = colour
#     def __str__(self):
#         return f"{self.name} is a human with {self.colour} coulor and {self.parent} is the parent of {self.name}"    
# person = human("bhoomi","mummy","white")
# print(person.name)
# print(person.parent)
# print(person.colour)
# print(person)
# print(person.__str__())
#--------------------------------------

class calculator:
    def add(self,a,b):
        return a+b
    def sun(self,a,b):
        return a-b
    def multi(Self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
ans = calculator()
a = int(input("enter value of first number "))
b = int(input("enter value of second number "))

print(ans.add(a,b))
print(ans.sun(a,b))
print(ans.multi(a,b))
print(ans.div(a,b))    
