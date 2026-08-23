#File modes

'''append mode'''
# f=open("File_Input_output/sample2.txt","a")

# data=f.write("hello guys")


'''write mode'''
#f=open("File_Input_output/sample3.txt","w")

# data=f.write("hello guys")

'''x mode'''
# f=open("File_Input_output/data.txt","x")

# data=f.write("hello guys")


'''r+ mode'''
# f=open("File_Input_output/sample.txt","r+")

# data=f.write("suman lata")
# print(f.read())

'''w+ mode'''
# f=open("File_Input_output/sample.txt","w+")

# data=f.write("suman lata")
# print(f.read())


'''a+ mode'''
f=open("File_Input_output/sample.txt","a+")

data=f.write("simran is a good girl")
print(f.read())



f.close()