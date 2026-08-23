#assignment 5

'''create a program that:
a. opens a file "names.txt" in write mode
b. write 5 names(one per line) entered by the user
c. then opens the same file in read mode and prints all names'''


'''a part'''
# with open("assignments/names.txt", "w") as f:
#   data=f.write("hello guys")


'''b part'''
# with open("assignments/names.txt", "w") as f:

#   for i in range(1,6):
#     name=input("enter name:")
#     data=f.write(name +"\n")


'''c part'''
# with open("assignments/names.txt", "r") as f:
#   data=True

#   while data:
#     data=f.readline()
#     print(data, end="")



'''create a program that:
a. adds a file "log.txt" in append mode
b. adds a new log entry (like "program run successfully")
c. opens the file in read mode and print all logs'''

# with open("assignments/log.txt", "a") as f:
#   f.write( "\n" + "program run successfully" + "")


# with open("assignments/log.txt", "r") as f:
#   data=f.read()
#   print(data)



'''create a program that:
1. has a list of numbers: [5, 10, 15, 20, 25]
2. uses a list comprehension to create a list with only number greater than 15
3. print the new list'''

# numbers=[5, 10, 15, 20, 25]
# ans=[]

# ans=[val for val in numbers if val>15]

# print(ans)


'''create a python dictionary of 3 cities and their populations. Save it to "cities.json"
1. then load the JSON and print each city and its population.
2. ask the user for a new city and its population -update this info in the json file'''


# import json
# with open("assignments/cities.json","r+") as f:
#   py_obj=json.load(f)
#   print(py_obj)

#   new_city=py_obj.update({
#     "noida":643734
#   })

#   f.seek(0)
#   json.dump(new_city, f)
#   f.truncate()

# print(py_obj)


'''write a program that tries to open "data.txt" in read mode. If the file does not exist, catch the exception and print "File not found!"
'''

try:
  with open("assignments/data.txt", "r") as f:
    data=f.read()
    print(data)

except FileNotFoundError:
  print("file not found!")

finally:
  print("end of assignment 5!")

  



