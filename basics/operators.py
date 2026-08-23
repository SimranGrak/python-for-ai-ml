#operators in python

a=10
b=5

#arithmetic operator
print("addition:", a+b)
print("subtraction:", a-b)
print("multiplication:", a*b)
print("division:", a/b)
print("modulo:", a%b)


#relational operator
print(a>=b)
print(a==b)
print(a>b)
print(a<b)
print(a<=b)
print(a!=b)
print(2==2) #we can compare values also instead of telling their names

#assignment operator
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b  
print(a)                     #my output is coming 10.0 because by previous operations my a=50
a%=b
print(a)
a**=b
print(a)                     #my output  would be 0.0 because the a value after previous operations becomes 0


#logical operator
#not logical operator
var=True 
print(not var)        #false
print(not (8>5))      #false 

#and logical operator
print((5>3) and (2>1))        #true
print((5>9) and (2>1))

#or logical operator
print((5>3) or (2>1))        #true
print((5>9) or (2>1))        #true