#functions in python

# def hello():                          #function definition
#   print("hello world")


# hello()                               #function call
# hello()




#create function to calculate sum of two numbers

# def sum(a,b):
#   s=a+b
#   return s

# ans=sum(3,5)
# print(ans)



#create a function that returns average of 3 numbers
# def average(a,b,c):
#   avg=(a+b+c)/3
#   return avg

# res=average(2,3,5)
# print(res)



#default parameters concept

def sumNum(b, a=1):
  sum=a+b
  return sum

answer=sumNum(5)
print(answer)
