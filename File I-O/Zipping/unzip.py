import zipfile
# Open zip file
z = zipfile.ZipFile('test.zip', 'r')

names = z.namelist()
for name in names:
    print 'Unzipping ' + name
    f = z.open(name)
	contents = f.read()
	print contents