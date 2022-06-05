from flask import Flask, request

app = Flask(__name__)


@app.route('/info', methods=['GET'])
def info():
    return '<h1>Mario Josue Solis Solorzano - 201900629</h1>'


if __name__ == '__main__':
    app.run(port=4000)