from flask import Flask, request, jsonify
from get_currenty import main
# from post_to_html import create_pdf
import json

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
    return f'{amount} {currency} to EUR is: {final_money}'


# @app.route('/translator', methods=['POST'])
# def translator():
#     if request.method == 'POST':
#         # posted_json = jsonify(request.get_json())
#         # print(posted_json.get('total'))
#         # create_pdf(request.get_json())
#         return 'PDF CREATED'
#     else:
#         return 'Hola GET'



if __name__ == "__main__":
    app.run(debug=True)