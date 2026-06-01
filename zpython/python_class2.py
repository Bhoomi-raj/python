# class human:
#     def __init__(self,name,gen,height):
#         self.name = name
#         self.gen = gen
#         self.height = height
#     def display(self):
#         print("name ",self.name)
#         print("gen ",self.gen)
#         print("height",self.height)    
# class boy(human):
#     def __init__(self,name,gen,height,course,college):
#         super().__init__(name,gen,height)  
#         self.course = course
#         self.college = college        
#     def display(self):
#         super().display()
#         print("course ",self.course)
#         print("college ",self.college)
# student = boy("abc","male",5,"cse","college")
# student.display()        
