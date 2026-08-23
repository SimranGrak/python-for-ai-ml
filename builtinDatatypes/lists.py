#lists in python


# marks=[56,99,96,75,89,76]

# print(marks)
# print(len(marks))


'''Print value at index 2'''
# print(marks[2])


'''value assignment in list'''
# marks[2]=97
# print(marks)


'''multiple type of data in list'''

# items=[90, "abc", 99.9, True]
# print(items)
# print(type(items))


'''slicing in lists'''
# print(marks[:5])
# print(marks[2:])
# print(marks[-5:-2])




'''loops with lists'''

# for val in marks:
#   print(val)


'''WAP to find index of 10 in list'''
l=[1,2,7,10,6,9]

idx=0
x=10

for val in l:
  if (val==x):
    print(f"{x} found at index {idx}")
    break

  idx+=1

  
