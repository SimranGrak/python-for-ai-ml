#assignment 2

'''WAP that take salary as input. Using conditional statements, calculate the final tax rate based on these rules:
a. if salary <30000 ->5%
b. if salary is 30000-70000:15%
c. if salary > 70000: 25%
'''
# salary=int(input("Enter salary: "))

# if (salary <30000):
#   print("TAX: 5%")

# elif (salary >=30000 and salary<=70000):
#   print("TAX: 15%")

# else:
#   print("TAX: 25%")



'''Write a function that takes two integers a and b and prints all even numbers between them (inclusive)'''
# def even(a,b):
#   for i in range(a,b+1):
#     if (i%2==0):
#       print(i)

# even(1,10)



'''write a function that prints the digits of a number n.'''
# def digits(n):
#   while n>0:
#     temp=n%10
#     remove=int(n/10)
#     n=remove
#     print(temp)


# digits(4516)


'''write a function to return the count the number of digits in a number n.'''
# def count(n):
#   n=str(n)
#   i=0
#   for ch in n:
#     i+=1
#   return i

# ans=count(66666)
# print("count is:", ans)



'''write a function to return the sum of digits of a number, n.'''
# def sum_digits(n):
#   n=str(n)
#   s=0
#   for i in n:
#     s+=int(i)
#   return s

# answer=sum_digits(1234)
# print("sum is:",answer)



'''write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.'''
# for i in range(1,101):
#   if (i%3==0 and i%5==0):
#     print(i)

#   else:
#     continue



'''design a program to continuously input a number n from user and print if it is positive or negative until the user enters 'Quits'.'''

# n=input("enter number(quit or exit):")

# while n!="Quit":
#   n=int(n)

#   if n>0:
#     print("positive!")

#   elif n<0:
#     print("negative!")

#   else:
#     print("zero!")

#   n=input("enter number(quit or exit):")



'''Lets create a simple calculator that performs arithmetic operations. create  a function calculator(a, b, operation) that peforms addition, subtraction, multiplication, or division based on  the operation parameter.
'''


# def calculator(a, b, operation):
#   if operation=="+":
#     sum=a+b
#     return sum

#   elif operation=="-":
#     difference=a-b
#     return difference

#   elif operation=="*":
#     multiply=a*b
#     return multiply

#   elif operation=="/":
#     if b==0:
#       return "Division by 0 is not allowed"
#     return int(a/b)

#   else:
#     return "enter valid operation"


# answer1=calculator(10,2,"/")
# print(answer1)



'''write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop'''
# def is_prime(n):
#   if n<=1:
#     return False

#   for i in range(2, n):
#     if n%i==0:
#       return False

#   return True

# print(is_prime(8))


'''Let's create a "Number Guessing Game". Given  a secret number (already decided by you), write a program that asks the user to guess it and prints:
a. "Too high" if the guess is above a number
b. "Too low" if the guess number is below
c. "Correct" if the guess matches
'''

user_guess=int(input("enter number:"))

secret_number=8

if user_guess>secret_number:
  print("Too high")

elif user_guess<secret_number:
  print("Too low")

else:
  print("Correct!")

