#print all the lines from file
fin=open("input.txt","r")      
for line in fin:
          print(line.strip())
fin.close()
