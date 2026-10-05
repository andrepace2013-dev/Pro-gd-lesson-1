# oops-objecct orionted programing structure
class Student:
    # init - inbuilt function to declare properties with the class
    def __init__(self,name,age,grade,favcolor,hobby):
        self.name=name
        self.age=age
        self.grade=grade
        self.favcolor=favcolor
        self.hobby=hobby
        self.intro=""

    def show_deatails(self):
         print("Name : ", self.name)
         print("age : ", self.age)
         print("grade : ", self.grade)
         print("favcolor : ", self.favcolor)
         print("hobby : ", self.hobby)
    def intro_student(self):
        self.intro=input('intrtoduce yourself?            ')
        print(self.intro)
# object 
s1=Student("Andre",13,9,"Red","Computing")

s1.show_deatails()
s1.intro_student()

s2=Student("Ben",13,9,"Green","Sports")

s2.show_deatails()
s2.intro_student()