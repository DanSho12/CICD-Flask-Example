from flask import request, Flask
import json

app = Flask(__name__)


@app.route('/plus_one')
def plus_one():
    x = int(request.args.get('x', 1))
    return json.dumps({'x': x + 1})


@app.route('/square')
def square():
    x = int(request.args.get('x', 1))
    return json.dumps({'x': x * x})


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return 'Hello! Try square or plus_one!'


if __name__ == '__main__':
    app.run(debug=False, port=8080, host='0.0.0.0', threaded=True)
