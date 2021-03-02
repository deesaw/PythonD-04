f=open("c:/users/tring/desktop/myfile.txt","a")

print f.name
print f.mode
print f.fileno()
print f.closed
f.write("hello")
f.write(" how are you?\n")
f.write("\n")
f.write("good morning")
f.close()
print f.closed
