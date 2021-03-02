from bottle import route, run
@route('/hello')
def hello():
    return "<h1> WELCOME TO WORLD OF PYTHON</h1>"
run(host='localhost', port=8080, debug=True)
