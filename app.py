from turtle import pos
from flask import Flask
from get_currenty import main

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/info/<user>')
def info(user):
    return "Hello: " + user


@app.route('/post/<post_id>')
def post(post_id):
    moco = int(post_id) + 4
    return "Post Number: " + str(moco)


@app.route('/conversor/<currency>-<amount>')
def currency(currency, amount):
    currency_info = main(currency)
    final_money = str(float(amount) * float(currency_info))
    print(final_money)
    return f'{amount} {currency} to EUR is: {final_money}'


if __name__ == "__main__":
    app.run(debug=True)