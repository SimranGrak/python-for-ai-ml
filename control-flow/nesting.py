#nesting in python: is another way of wring conditional statement is better way

#WAP to print the categories of age
# age=int(input("enter age:"))

# if age<13:
#   print("child!")

# else:
#   if (age >=13 and age< 18):
#     print("teenager!")

#   else:
#     print("adult!")


#WAP to validate user credentials to login

username=input("enter username:")
password=input("enter password:")

if (username=="admin" and password=="pass"):
  print("success!")

else:
  if username!="admin":
    print("wrong username!")

  else:
    print("wrong password!")