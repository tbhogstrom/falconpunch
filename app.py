from bottle import Bottle, run, template, static_file

app = Bottle()

# Home page route
@app.route('/')
def index():
    return template('index.html')

# Static file route
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

if __name__ == "__main__":
    run(app, host='localhost', port=8080)