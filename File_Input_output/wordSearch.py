#word search activity

'''write a program to read python in file and print the line number'''

line=1
word="python"
data=True

with open("File_Input_output/sample.txt", "r") as f:
  while data:
    data=f.readline()

    if (word in data):
      print(f"{word} found at {line}")
      break

    print(data)
    line+=1



