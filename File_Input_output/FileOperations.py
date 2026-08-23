#File operations

# f=open("File_Input_Output/sample.txt", "r")

'''read mode of complete file'''
# data=f.read()
# print(data)
# print()

'''reading file line by line'''
# data=f.readline()
# print(data)

'''overwriting file'''
f=open("File_Input_output/sample.txt","w")
data=f.write("hii guys \nlets do a practice of dance!")

f.close()