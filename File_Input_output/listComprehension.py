#list comprehensions

'''write a list from 0 to 6 in which we store squares of numbers'''
'''traditional way'''
# squares=[]

# for i in range(6):
#   squares.append(i*i)
# print(squares)


'''with list comprehensions'''
# sq=[i*i for i in range(6)]
# print(sq)


'''make a list that store square of odd numbers only from 0 to 5'''
# sq=[i*i for i in range(6) if i%2!=0]
# print(sq)


'''given a list in which replace negative values with zeros'''
# lis=[-2,6,-6,8,-2,9,-5]


# lis=[0 if val<0 else val for val in lis]
# print(lis)


'''given a list and coonvert them into upper case'''
lis=["hello", "python", "apnacollege"]

lis=[val.upper() for val in lis]
print(lis)

