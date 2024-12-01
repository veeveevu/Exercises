#13.1

from flask import Flask, jsonify

app = Flask(__name__)

def check_prime_number(num):
    num = int(num)
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

@app.route('/prime_number/<int:input_number>')
def prime_number(input_number):
    result = {
        "Number" : input_number,
        "isPrime" : check_prime_number(input_number)
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)