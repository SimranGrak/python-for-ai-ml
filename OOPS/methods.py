#methods in python


class Student:
  college_name="ABC college"

  def __init__(self, name, cgpa):
    self.name=name
    self.cgpa=cgpa

  #class method
  @classmethod
  def get_college(cls):
    print(f"college name is: {cls.college_name}")

  #instance method
  def get_info(self):                  
    print(f"{self.name} study in {self.college_name} and got {self.cgpa}")

  #static method
  @staticmethod
  def cal_discount(fee, discount):
    final_fee=int(fee-(fee*discount)/100)
    print(f"final fee is: {final_fee}")


stu1=Student("simran",9.9)
stu1.get_info()
stu1.get_college()
Student.get_college()
stu1.cal_discount(40000,10)
    