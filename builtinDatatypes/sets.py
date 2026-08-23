#sets in python

# s={1,2,2,3,3}

# print(s)
# print(type(s))

'''empty set'''
# empty_set=set()
# print(type(empty_set))
# print(empty_set)


'''Practice question in sets
Given a list of tuples with info(name, subject):
a. list all unique courses
b. list students enrolled in english
c. create dictionary (student, set of courses)
'''
info=[
  ("Alice", "Math"),
  ("Bob", "Science"),
  ("Alice", "Science"),
  ("Charlie", "Math"),
  ("Bob", "Math"),
  ("Alice", "English"),
  ("Charlie", "English"),
]

'''part a'''
# set_courses=set()
# for name,course in info:
#   set_courses.add(course)
# print(set_courses)

'''part b'''
# for name, course in info:
#   if (course=="English"):
#     print(name)

'''part c'''

new_dict={}
for name, course in info:
  if (new_dict.get(name)==None):
    new_dict.update({name:set()})
    new_dict[name].add(course)

  else:
    new_dict[name].add(course)

print(new_dict)




