#File handling

my_file=open("input.txt","r")
print my_file.read()
my_file.close()

#how to seek within a file
To move to the beginning of a file
f.tell() #gives the current position

f.seek(a,b)
a=integer
b=0#from start
b=1#from current position
b=2#from end





f=open("text.txt","r+")
print f.tell()		#gives the current position
print f.readline()	#reads a line from file
print f.tell()		#gives the current position
f.seek(0,0)			#moves the file pointer to the beginning of file
print f.tell()		#gives the current position
print f.readline()	#reads a line from file
f.close()




















my_file=open("text.txt","r+")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()























f = open("output.txt", "w")
print f
f.write("This is line1\n")
f.write("This is line2\n")
f.write("This is line3\n")
f.close()





















To move to the beginning of a file
f.tell() #gives the current position
f.seek(a,b)
a=int
b=0#from start
b=1#from current position
b=2#from end




















Status check
f.closed #gives True if file is closed

















#No worries about closing a file
with open("text.txt","w") as my_file:
	my_file.write("I love vegetables")
