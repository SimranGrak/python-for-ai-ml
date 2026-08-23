#Encapsulation in OOP
class BankAccount:

  def __init__(self, name, balance, accID):
    self.name=name                   #public attribute
    self._balance=balance            #protected attribute
    self.__accID=accID               #private attribute


  '''get account ID'''
  def get_accID(self):
    return self.__accID

  '''set account ID'''
  def set_accID(self, newaccID):
    self.__accID=newaccID
  


acc1=BankAccount("simran",100000, 5463271823718)
acc1.set_accID(15267899237189)
print(acc1.name, acc1._balance, acc1.get_accID())
    