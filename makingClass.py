from operator import truediv

#class

class Student:
     def __init__(self,name,grade,age):
         self.name=name
         self.grade=grade
         self.age=age

     def get_info(self):
        return f"The student name is {self.name}, age is {self.age}  and is has grade of {self.grade}"

     def is_passed(self):
         if self.grade>=60:
             return True
         else:
             return False

#object
s1=Student("Anuska", 90,24)
s2=Student("Pranika", 87,22)
s3=Student("Kendrika", 57,23)

print(s1.get_info())
print(f"Is student passed? {s1.is_passed()}")
print(s2.get_info())
print(f"Is student passed? {s2.is_passed()}")
print(s3.get_info())
print(f"Is student passed? {s3.is_passed()}")

