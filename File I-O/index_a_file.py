f=open('pledge.txt','r')
words=[]
for line in f:
    words.extend(line.rstrip().split(' '))
finalwords=[]
for word in words:
	if len(word)>3:
		finalwords.append(word)

words=[]
finalwords.sort()
uniquewords=set(finalwords)
for word in uniquewords:
	words.append((word,finalwords.count(word)))

for word,count in words:
	print "Word ",word," repeats ",count," times"


		
f.close
