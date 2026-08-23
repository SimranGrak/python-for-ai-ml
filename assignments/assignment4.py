#assignment 4

'''create a BankAccount class with attributes account_number, owner_name and balance.
Add method to deposit, withdraw, and check_balance'''

# class BankAccount:
#   def __init__(self, account_number, owner_name, balance):
#     self.owner_name=owner_name
#     self._account_number=account_number
#     self.__balance=balance

#   def deposit(self, add_money):
#     self.__balance+=add_money
#     return self.__balance

#   def withdraw(self, withdraw_money):
#     self.__balance-=withdraw_money
#     return self.__balance

#   def check_balance(self):
#     return self.__balance


# Acc1=BankAccount(5327189347328, "simran", 7000)
# print(Acc1.deposit(2000),Acc1.withdraw(1000), Acc1.check_balance())


'''create a class Book with the following attributes:
a. title
b. author
c. list of reviews

And add methods to:
a. add a new review
b. count reviews
c. diplay all reviews'''


# class Book:
#   def __init__(self, title, author):
#     self.title=title
#     self.author=author
#     self.reviews_list=[]

#   def add_review(self, new_review):
#     self.reviews_list.append(new_review)

#   def count_review(self):
#     return len(self.reviews_list)

#   def display_reviews(self):
#     for i in self.reviews_list:
#       print(i)

# B1=Book("seven wonders","simran")
# B1.add_review("great!")
# B1.add_review("superb!")
# B1.add_review("Good!")
# print(B1.title, B1. author)
# print(B1.count_review())
# print("All reviews")
# B1.display_reviews()


'''create a class student with private attributes _name, _roll_no, and marks.
provide getter and setter methods with validation (e.g. marks cannot be negative, roll number has to be between 1 &100 & name cannot be empty).'''

# class Student:
#   def __init__(self, name, roll_no, marks):
#     self.__name=name
#     self.__roll_no=roll_no
#     self.__marks=marks

#   def get_name(self):
#     return self.__name

#   def get_marks(self):
#     return self.__marks

#   def get_roll_no(self):
#     return self.__roll_no

#   def set_name(self, new_name):
#     if (new_name)=="":
#       print("name cannot be empty!")

#     else:
#       self.__name=new_name

#   def set_marks(self, new_marks):
#     if(new_marks<=0):
#       print("marks cannot be negative!")

#     else:
#       self.__marks=new_marks

#   def set_roll_no(self, new_roll_no):
#     if (new_roll_no>=1 and new_roll_no<=100):
#       self.__roll_no=new_roll_no

#     else:
#       print("roll number has to be between 1 &100")

# S1=Student("simran",23, 98)
# print(S1.get_name(), S1.get_marks(), S1.get_roll_no())

# S1.set_marks(24)
# print(S1.get_marks())

# S1.set_name("robin")
# print(S1.get_name())

# S1.set_roll_no(1)
# print(S1.get_roll_no())
# print(S1.get_name(), S1.get_marks(), S1.get_roll_no())


'''Create a class Shape with a method area()
Create subclass Circle, Rectangle, and Triangle that override the area() method.'''

# class Shape:
#   def area(self):
    #pass

# class Circle(Shape):
#   def area(self, radius):
#     print(f"area of circle={3.14*radius*radius}")

# class Rectange(Shape):
#   def area(self, length, width):
#     print(f"area of rectangle={length*width}")

# class Triangle(Shape):
#   def area(self, base, height):
#     print(f"area of traingle={1/2*(base/height)}")

# C1=Circle()
# C1.area(2)

# R1=Rectange()
# R1.area(2,3)

# T1=Triangle()
# T1.area(10,2)


'''Create a base class vehicle with attributes like brand and model.
Create two subclasses Car and Bike that add extra attributes- seats (in car) and engine-cc(in Bike)'''

# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand=brand
#     self.model=model

# class Car(Vehicle):
#   def __init__(self, brand, model,seats):
#     super().__init__(brand, model)
#     self.seats=seats

# class Bike(Vehicle):
#   def __init__(self, brand, model, engine_cc):
#     super().__init__(brand, model)
#     self.engine_cc=engine_cc


# C1=Car("BMW",20.1,4)
# print(C1.brand, C1.model, C1.seats)

# B1=Bike("splender",8.2, "32")
# print(B1.brand, B1.model, B1.engine_cc)
    

'''Create a abstract class Employee with an abstract method calculate_salary().
Create  subclasses Intern, FullTimeEmployee, and ContractEmployee that implement the method differently'''

# from abc import ABC, abstractmethod

# class Employee(ABC):
#   @abstractmethod
#   def calculate_salary(self):
#     pass

# class Intern(Employee):
#   def calculate_salary(self):
#     print("salary= 10000/month")

# class FullTimeEmployee(Employee):
#   def calculate_salary(self):
#     print("salary=20000/month")

# class ContractEmployee(Employee):
#   def calculate_salary(self):
#     print("salary=15000/month")

# Int=Intern()
# Int.calculate_salary()

# FullTime=FullTimeEmployee()
# FullTime.calculate_salary()

# Contract=ContractEmployee()
# Contract.calculate_salary()


'''create a class Person that allows the constructor to work with:
a. name only
b. name + age
c. name + age + address

As direct constructor overloading (multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading.'''


# class Person:
#   def __init__(self, name, age=None , address=None):
#     self.name=name
#     self.age=age
#     self.address=address

#   def display(self):
#     print("name:", self.name)
#     print("age:", self.age)
#     print("address:",self.address)

# P1=Person("bob")
# P1.display()
# print()

# P2=Person("adam", 23)
# P2.display()
# print()

# P3=Person("eva",22, "Sunnyvale")
# P3.display()



'''Create a class Player with:
a. a class variable player_count
b. instance variables name and level
Track how many players were created'''

# class Player:
#   player_count=0

#   def __init__(self, name, level):
#     self.name=name
#     self.level=level
#     Player.player_count+=1

#   @classmethod
#   def count(cls):
#     print(f"total players are :{cls.player_count}")

# P1=Player("simran",2)
# P2=Player("robin",3)
# P3=Player("suman",3)
# print(P1.name, P1.level)
# print(P2.name, P2.level)
# print()
# Player.count()



'''create the following classes: Herbivore, Carnivore, Omnivore with some attributes and methods. Then create a class Bear that inherits from all the above classes to showcase how multiple inheritance works.'''


# class Herbivore:

#   def __init__(self, name):
#     self.name=name
    
#   def diet(self):
#     print("eat plants!")

# class Carnivore:

#   def __init__(self, food):
#     self.food=food
    
#   def animals(self):
#     print("lion is example of Carnivore!")

# class Omnivore:

#   def __init__(self, location):
#     self.location=location

#   def habits(self):
#     print("eat both plants and animals!")

# class Bear(Herbivore, Omnivore, Carnivore):
#   def __init__(self, name, type, food, location):
#     super().__init__(name)
#     Carnivore.__init__(self,food)
#     Omnivore.__init__(self,location)
#     self.type=type


# B1=Bear("Bobby","Animal", "meat", "Amazon jungle")
# print(B1.name, B1.type, B1.food, B1.location)

# B1.diet()
# B1.animals()
# B1.habits()


'''Mini Project-OOP Chat System
Let's create a chat system using OOPs concepts. We have to create classes.
a. user
b. message
c. chatRoom

And we have to implement functions:
a. sending messages
b. viewing chat history
c. user joining and leaving the chatroom'''

class Message:
  message_count=1

  def __init__(self, sender, content):
    self.sender=sender
    self.content=content
    self.id=Message.message_count
    Message.message_count+=1

  def __str__(self):
    return f"{self.id}: {self.sender.username}-{self.content}"

class User:
  def __init__(self,username):
    self.username=username
    self.chatRoom=None

  def join_chatRoom(self, chatRoom):
    if self.chatRoom:
      print(f"{self.username} already exist in chatRoom!")

    else:
      chatRoom.add_user(self)
      self.chatRoom=chatRoom
      print(f"{self.username} joined {self.chatRoom.name}")

  def leave_chatRoom(self):
    if self.chatRoom:
      self.chatRoom.remove_user(self)
      self.chatRoom=None
      print(f"{self.username} removed from chatRoom!")

    else:
      print(f"{self.username} does not exist in chatRoom!")

  def send_message(self,content):
    if not self.chatRoom:
      print(f"{self.username} cannot send message(not in chatRoom)!")

    else:
      self.chatRoom.broadcast(self, content)


class ChatRoom:
  def __init__(self, name):
    self.name=name
    self.users=[]
    self.messages=[]

  def add_user(self, user):
    self.users.append(user)

  def remove_user(self, user):
    self.users.remove(user)

  def broadcast(self, sender, content):
    message=Message(sender, content)
    self.messages.append(message)

  def display_messages(self):
    print("\n Display all messages")
    for msg in self.messages:
      print(msg)
      print()


room=ChatRoom("Python chatRoom")

U1=User("simran")
U2=User("eva")

U1.join_chatRoom(room)
U2.join_chatRoom(room)

U1.send_message("hello eva!")
U2.send_message("hello simran!")

room.display_messages()
















  
    
    