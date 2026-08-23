#with keyword

with open("File_Input_output/data.txt", "r") as f:
  data=f.read()
  print(data)
  print(len(data))