f=open("input.txt","a")

print(f.name)         #prints name of the file
print(f.mode)         #prints the file mode  
print(f.closed)       #Returns true if the file is closed else false
f.seek(3)             #sets the current position at the offset
print(f.tell())       #current position of the pointer
f.close()             #Closes the file
print(f.closed)        

