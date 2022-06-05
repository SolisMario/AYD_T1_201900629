from flask import Flask, request

app = Flask(__name__)


@app.route('/suma', methods=['POST'])
def suma():
    num1 = request.json['num1']
    num2 = request.json['num2']
    sum = num1 + num2
    return {'resultado': sum}


if __name__ == '__main__':
    app.run(port=3000)
