#match case is alternate of if, else, elif statements

#traffic lights using match case statement
color=input("enter color:")

match color:
  case "Green":
    print("Go!")
  case "Yellow":
    print("Wait!")
  case "Red":
    print("Stop!")
  case _:
    print("wrong color!")