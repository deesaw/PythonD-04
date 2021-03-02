f=open('words.txt','r')
words={}
for line in f:
	pos=line.index('=')
	word=line[:pos]
	meaning=line[pos+1:].rstrip()
	words[word]=meaning
f.close()