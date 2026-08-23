#abstraction in OOP
from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def make_sound(self):
    pass

class Lion(Animal):
  def make_sound(self):
    print("Roar!")

class Cat(Animal):
  def make_sound(self):
    print("Meow!")


L1=Lion()
L1.make_sound()

C1=Cat()
C1.make_sound()
