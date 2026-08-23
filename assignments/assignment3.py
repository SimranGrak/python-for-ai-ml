#assignment 3

'''ask the user for a string and check whether it is palindrome or not.'''
# string=input("enter a string:")  

# slicing=string[::-1]        
# if string==slicing:
#   print("palindrome!")
# else:
#   print("not palindrome!")

'''or'''

# reverse=""
# for ch in string:
#   reverse=ch+reverse
# if reverse==string:
#   print("yes!")
# else:
#   print("no!")


'''given a list of integers compute the average of all numbers in the list'''

# list=[1,2,4,5,6,7]

# list_len=len(list)
# sum=0
# for i in list:
#   sum+=i

# avg=sum/list_len
# print(f"average of list is {avg}")


'''input two lists of integers from the user. Merge them into one list and sort the result.'''

# list1=list(map(int,input("enter first list:").split()))
# list2=list(map(int,input("enter second list:").split()))

# result=list1+list2
# result.sort()
# print(f"sorted list is: {result}")


'''given a tuple of integers, create:
a. a tuple of all even numbers
b. a tuple of all odd numbers'''

# tup=(1,3,4,6,4,3,2,6,8,9)
# even_list=[]
# odd_list=[]

# for i in tup:
#   if (i%2==0):
#     even_list.append(i)

#   else:
#     odd_list.append(i)

# even_tuple=tuple(even_list)
# odd_tuple=tuple(odd_list)
# print(f"all even number: {even_tuple}")
# print(f"all odd number: {odd_tuple}")


'''Create a dictionary where:
a. keys=student names
b. values=marks(integer)
write a menu-based program where user presses a key('A','B','C','D') depending on the operation they want to perform on the dictionary:
a. A- add a student
b. B- update marks
c. C- search for a student
d. D- display all students and marks 
'''
# new_dict={
#   "simran":98,
#   "robin":99,
#   "punjab":97,
#   "suman":94
# }

# print("a. A- add a student \nb. B- update marks \nc. C- search for a student \nd. D- display all students and marks ")

# option=input("Enter a choice:")

# while(option!="Quit"):
#   if(option=='A'):
#     name=input("enter name:")
#     marks=int(input("enter marks:"))

#     if (new_dict.get(name)!=None):
#       print("user already exist!")
#       option=input("Enter a choice:")
#     else:
#       new_dict.update({name:marks})
#       print(new_dict)
#       option=input("Enter a choice:")

#   elif(option=='B'):
#     name=input("enter name:")
#     if (new_dict.get(name)!=None):
#       marks=int(input("enter marks:"))
#       new_dict.update({name:marks})
#       print(new_dict)
#       option=input("Enter a choice:")

#     else:
#       print("User does not exist!")
#       option=input("Enter a choice:")

#   elif(option=='C'):
#     name=input("enter name:")
#     if (new_dict.get(name)!=None):
#       print(f"{name} marks are: {new_dict.get(name)}")
#       option=input("Enter a choice:")

#     else:
#       print("user does not exist!")
#       option=input("Enter a choice:")

#   elif(option=='D'):
#     print(new_dict)
#     option=input("Enter a choice:")

#   else:
#     print("Choose valid option!")
#     option=input("Enter a choice:")


# print("Exiting program... \nThank you!")



'''Given a lsit of words:
create a dictionary that maps each word to its length'''

# word=["apple", "banana", "kiwi", "cherry", "mango"]

# new_dict={}

# for i in word:
#   length=len(i)
#   new_dict.update({i:length})

# print(new_dict)


'''write a program that takes a string from the user and prints the number of spaces in the string'''

# string=input("enter a string:")

# count=0
# for ch in string:
#   if(ch==" "):
#     count+=1

# print(f"count of spaces in the string are {count}")


'''write a program to check whether two lists share no common elements'''

# list1=list(map(int,(input("enter first list:").split())))
# list2=list(map(int,(input("enter second list:").split())))

# set1=set(list1)
# set2=set(list2)

# common=set1.intersection(set2)

# if (common==set()):
#     print("share no common!")

# else:
#     print("share common!")


'''given a list, print all elements that appear more than once in the list'''
# list=list(map(int,input("enter a list:").split()))

# seen=set()
# duplicate=set()
# for i in list:
#   if i in seen:
#     duplicate.add(i)
#   else:
#     seen.add(i)

# print(f"duplicates are: {duplicate}")


'''ask the user for a string and print
a. all unique characters
b. the count of unique characters'''

string=input("enter a string:")

new_string=set(string)
print(len(new_string))
print(new_string)








      



