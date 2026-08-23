#constructor in python
class Student:
  def __init__(self, name, cgpa):
    self.name=name
    self.cgpa=cgpa

  def get_cgpa(self):
    print(f"{self.name} has {self.cgpa}")


stu1=Student("simran",9.6)
stu2=Student("robin",9.9)
stu1.get_cgpa()
stu2.get_cgpa()
print(stu1.name, stu1.cgpa)
print(stu1.name, stu1.cgpa) 

    