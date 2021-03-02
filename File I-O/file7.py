f=open("wells.txt","r")			#open the file in read mode
for line in f:					#read the line
	word,meaning=line.split('=')#split the line on =
	print word					#get the word part (first part)
f.close()						#close the file