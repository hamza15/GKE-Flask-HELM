from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/will')
def helloIndex():
    response = 'Hello World'
    return jsonify(response)

@app.route('/ready')
def readyIndex():
    response = 'It works!'
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)
