#print all the lines which starts with smile
fin=open("input.txt","r")      
for line in fin:
    if (line.lower()).startswith('smile'):
            print(line.strip())
fin.close()

#Write a program to print all the lines which ends with beautiful
#endswith



