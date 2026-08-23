#Inheritance in OOP

# class Employee:
#   start_time="9:30AM"
#   end_time="5:30PM"

#   def change_time(self, new_end_time):
#     self.end_time=new_end_time

# class Teacher(Employee):
#   def __init__(self, subject):
#     self.subject=subject

# class Admin(Employee):
#   def __init__(self, role):
#     self.role=role


# t1=Teacher("maths")
# t1.change_time("6PM")
# print(t1.start_time, t1.end_time, t1.subject)

# staff1=Admin("manager")
# print(staff1.role, staff1.end_time, staff1.start_time)



'''Multi level inheritance'''
# class Employee:
#   start_time="9:30AM"
#   end_time="5:30PM"

# class Admin(Employee):
#   def __init__(self, role):
#     self.role=role

# class Accountant(Admin):
#   def __init__(self, role, salary):
#     super().__init__(role)
#     self.salary=salary


# accountant1=Accountant("manager", 19000)
# print(accountant1.salary, accountant1.role)



'''Multiple Inheritance'''
class Teacher:
  def __init__(self, salary):
    self.salary=salary

class Student:
  def __init__(self, gpa):
    self.gpa=gpa

class TA(Teacher, Student):
  def __init__(self, salary, gpa, name):
    super().__init__(salary)
    Student.__init__(self, gpa)
    self.name=name

TA1=TA(70000, 9.6, "simran")
print(TA1.salary, TA1.gpa, TA1.name)