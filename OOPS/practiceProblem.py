#practice problem
'''design and create an online store for Products(name, price)
Track total products being created
Create a static method to calculate discount on each product based on a % parameter'''

class Product:
  total_product=0

  def __init__(self, name, price):
    self.name=name
    self.price=price
    Product.total_product+=1

  @classmethod
  def count_products(cls):
    print(f"Total products created are {cls.total_product}")

  @staticmethod
  def cal_discount(price, discount):
    print(f"discount price is {price-(price*discount/100)}")


product1=Product("macbook",150000)
product2=Product("iphone17",120000)
product3=Product("ipad",90000)
Product.count_products()
product1.cal_discount(product1.price, 10)


    