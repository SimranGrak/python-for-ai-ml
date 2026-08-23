#polymorphism in OOP

'''function overriding'''

# class Employee:
#   def get_designation(self):
#     print("Designation=Employee")

# class Teacher(Employee):
#   def get_designation(self):
#     print("Designation=Teacher")

# T1=Teacher() 
# T1.get_designation()


'''Duck Typing'''

class Teacher:
  def get_designation(self):
    print("designation=Employee")

class Accountant:
  def get_designation(self):
    print("designation=Accountant")

T1=Teacher()
T1.get_designation()

A1=Accountant()
A1.get_designation()