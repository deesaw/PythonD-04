import os,glob,zipfile
os.chdir('Y:/')				#go where the files are
pyfiles=glob.glob('*.py')	#select the files to zip
#and zip them
f=zipfile.ZipFile('fidelity-7-aug.zip','w')#open a zip archive
for file in pyfiles:		#add files to the archive
	f.write(file,compress_type=zipfile.ZIP_DEFLATED)
f.close()					#close the archive