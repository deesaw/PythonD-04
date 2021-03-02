import random
def tmpfilename():
	return str(random.random())[2:] + ".txt"
def file2paras(filename):
	para_begin = True
	with open(filename,"r") as f:
			outfile = open(tmpfilename(),"w")
			for lineno,line in enumerate(f):
					outfile.write(line)
					if len(line) == 1:
						para_begin=False
						outfile.close()
						outfile = open(tmpfilename(),"w")
