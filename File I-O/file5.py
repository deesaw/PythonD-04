f=open("c:/users/tring/desktop/wells1.txt","a")
a=["one\n","two\n","three\n","four\n","five"]
f.writelines(a)
f.flush()
f.close()
