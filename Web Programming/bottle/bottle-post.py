from bottle import run,route,request

@route('/add')
def showform():
	return """
<html>
<form method=post action="http://localhost:8090/addbook">
<input type=text name=id>Id<br>
<input type=text name=bookname>Book name<br>
<input type=text name=author>Author<br>
<input type=submit>
</form>
</html>

	"""

	
	
	
	
	
	
	
	
	
	
	
@route('/addbook', method='POST')
def login():
	import sqlite3
	conn = sqlite3.connect("mydatabase.db")
	cursor = conn.cursor()
	id=request.forms.get('id')
	bookname=request.forms.get('bookname')
	author=request.forms.get('author')
	sql="INSERT INTO books VALUES ({}, '{}','{}')".format(id,bookname,author)
	cursor.execute(sql)
	conn.commit()
	conn.close()
	return "<a href=/books>Book List</a>"

run(host='localhost',port=8090,debug=True)


