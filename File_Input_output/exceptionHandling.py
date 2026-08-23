#exception handling

try:
  x=int(input("enter x:"))
  ans=10/x

except ZeroDivisionError:
  print("division by zero is not allowed")

except ValueError:
  print("only integer value is allowed")

else:
  print(f"answer is: {ans}")

finally:
  print("end of our python program!")

