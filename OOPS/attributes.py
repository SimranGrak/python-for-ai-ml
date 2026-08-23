#class attributes and instance attributes in python

class Student:
  college_name="ABC college"                   #class attributes

  def __init__(self, name, cgpa):              #instance attributes
    self.name=name
    self.cgpa=cgpa

stu1=Student("simran", 9.8)
print(stu1.name, stu1.cgpa)
print(Student.college_name)
print(stu1.college_name)