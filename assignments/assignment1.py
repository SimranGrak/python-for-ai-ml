#assignment 1
'''WAP that asks the user for their name and age, then prints a sentence like:'''
# name=input("enter your name:")
# age=int(input("enter your age:"))

# print("hello", name,", you are", age, "years old!")



'''take two numbers as input from users and print their sum, difference, product, quotient'''
# a=int(input("enter value of a:"))
# b=int(input("enter value of b:"))

# sum=a+b
# difference=a-b
# product=a*b
# quotient=a%b

# print("sum is:", sum)
# print("difference is:", difference)
# print("product is:", product)
# print("quotient is:", quotient)




'''ask the user to enter two integers and one float. convert them all to floats and print their average'''
# c=int(input("enter value of c:"))
# d=int(input("enter value of d:"))
# e=float(input("enter value of e:"))

# float(c)
# float(d)

# avg=(c+d+e)/3
# print("average is:", avg, type(avg))



'''the user enters a string containing a number(e.g: "45"). convert it to:
a. an integer
b. a float
c. a string again
print all three values with their types
'''
# number=input("enter number:")

# integer_type=int(number)
# float_type=float(number)
# string_type=number

# print("an integer:",integer_type, type(integer_type))
# print("an float:", float_type,type(float_type))
# print("an string:",string_type, type(string_type))



'''evaluate and print the result of the following expression:
x=10+3*2**2
based on what you learnt in the lecture explain why the output is what it is.
'''
# x=10+3*2**2
# print(x)



'''WAP to swap values of two numbers entered by user.'''
# y=int(input("enter value of y:"))
# z=int(input("enter value of z:"))

# temp=y
# y=z
# z=temp

# print("y value:", y)
# print("z value:", z)



'''ask the user for a temperature in celcius(string input). convert it to float, then calculate and print temperature in fahrenheit.
conversion formula=fahrenheitTemp=(celciusTemp *(9/5))+32
'''
# temperature=input("enter temperature:")

# temperature=float(temperature)
# fahrenheitTemp=(temperature*(9/5))+32

# print("fahrenheit temperature:", fahrenheitTemp)



'''take the radius(r) as user input and print the area.
use the formula: Area=3.14*r**2
'''

# radius=int(input("enter the value of radius:"))

# Area=3.14*(radius**2)

# print("area is:", Area)


'''ask the user for: Principal(P), Rate(R), Time(T). Convert all to float and then compute simple interest.
SI=(P*R*T)/100
'''
# P=input("enter value of Principal:")
# R=input("enter value of Rate:")
# T=input("enter value of Time:")

# P=float(P)
# R=float(R)
# T=float(T)

# SI=(P*R*T)/100
# print("simple interest is:", SI)



'''take a decimal number as input (like 45.78) and output is:
a. integer part: 45
b. fractional part: .78
'''

number1=float(input("enter decimal number:"))

integer_part=int(number1)
fractional_part=number1-integer_part

print("integer_part", integer_part)
print("fractional_part", fractional_part)