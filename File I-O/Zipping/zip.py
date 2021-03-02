import zipfile

# Create zip file
f = zipfile.ZipFile('test.zip', 'w')

# add some files
f.write('file1.txt')

# add file as a new name
f.write('file2.txt', 'file-two.txt')

# add content from program (string)
f.writestr('file3.txt', 'Hello how are you')

# flush and close
f.close()