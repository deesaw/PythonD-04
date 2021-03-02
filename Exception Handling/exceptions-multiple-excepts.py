#Catching multiple exceptions
try:
	open a file
	connect to a database
except: I/O error
	Handle the i/o error
except: (database error,network error)
	Handle the database error
finally:
	if f.closed == False:close file 
	disconnect from database