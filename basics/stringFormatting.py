#string formatting in python
# a=5
# b=10
# sum=a+b

'''normal formatting'''
# print("sum of {} and {} is {}".format(a,b,sum))

'''index based formatting'''
# print("sum of {1} and {0} is {2}".format(a,b,sum))

'''value based formatting'''
# print("value of vars are {a} and {b}".format(a=1, b=5))




#f-strings in python
c=5
d=10

print(f"sum of {c} and {d} is {c+d}")

'''calculate average of 2 numbers using f-strings'''
print(f"average of {c} and {d} is {(c+d)/2}")