#Writes sequence of strings to file
data = ["hello Hyderabad\n", "Its going to rain today\n"]
fin = open("input2.txt", "w")
print("Name of the file: ", fin.name)
line = fin.writelines( data )
fin.close()
