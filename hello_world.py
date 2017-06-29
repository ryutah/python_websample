from bottle import route, run, template


@route('/hello')
def hello():
    return template("Hello {{string}}", string="World")

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True, reloader=True)
