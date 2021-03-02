my_file=open("input.txt","w")
my_file.write('hello')
my_file.write(' chennai\n')

lines=['hello\n','hai\n']
my_file.writelines(lines)

my_file.close()



my_file=open("text.txt","r+")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()













my_file=open("input.txt","r")
while True:
    myline=my_file.readline()
    if len(myline)<1:
            break
    print myline.rstrip()
f.close()
my_file.close()

my_file=open("input.txt","r")
while True:
    mychar=my_file.read(1)
    if len(myline)<1:
            break
    print mychar
f.close()
my_file.close()

my_file=open("input.txt","r")
mylist= my_file.readlines()
for line in mylist:
	print line.rstrip()
my_file.close()














my_file=open("text.txt","r")
print my_file.tell() #gives the current position
print my_file.readline()
print my_file.tell()
my_file.seek(0,0)
print my_file.tell()
print my_file.readline()
my_file.close()










f = open("output.txt", "w")
print f
print type(f)
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


f.seek(10,1)






Status check
f.closed #gives True if file is closed
