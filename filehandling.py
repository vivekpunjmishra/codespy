# f=open("file.txt","r")
# for data in f:
#     print(data)
#------------------------------------------------------------
# file = open("file.txt", "r") 
# print (file.read())
#------------------------------------------------------------
# file = open('file.txt','w')
# file.write("This is the write command")
# file.write("It allows us to write in a particular file")
# file.close()
#------------------------------------------------------------

# Python code to illustrate append() mode
file = open('file.txt','a')
file.write("This will add this line")
file.close()
