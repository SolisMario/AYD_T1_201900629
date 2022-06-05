from flask import Flask, request

app = Flask(__name__)


@app.route('/info', methods=['GET'])
def info():
    return '<h1>Mario Josue Solis Solorzano - 201900629</h1>'


@app.route('/info-curso', methods=['GET'])
def info():
    return '<h1>Analisis y Diseño 1 - Vacaciones Junio 2022</h1>'


if __name__ == '__main__':
    app.run(port=4000)