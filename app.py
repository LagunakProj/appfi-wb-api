
from flask import Flask, request, jsonify, render_template
from get_currenty import main
import json
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route('/user/<user>')
def user(user):
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


@app.route('/translator', methods=['POST'])
def translator():
    if request.method == 'POST':
        # posted_json = jsonify(request.get_json())
        # print(posted_json.get('total'))
        # create_pdf(request.get_json())
        return 'PDF CREATED'
    else:
        return 'Hola GET'


# @app.route('/info')
# def info():
#     return (render_template('home.html', nombre='te', mail='mailtest@gmail.com', listTest=['1', '2', '3']))


# @app.route('/jsontest/<user>', methods=['POST', 'GET'])
# def jsontest(user):
#     ahora = datetime.now()
#     d2 = ahora.strftime("%Y-%m-%d")

#     movesList = {'OCIO': {"test1": {
#         "ID": "0",
#         "CreatedAt": "20-10-2022",
#         "Title": "title test 1",
#         "Amount": "20"
#     },
#         "test2": {
#         "ID": "1",
#         "CreatedAt": "20-10-2022",
#         "Title": "title test 2",
#         "Amount": "27"
#     },
#     },
#         'SALUD': {"test1_salud": {
#             "ID": "2",
#             "CreatedAt": "20-10-2022",
#             "Title": "title test salud 1",
#             "Amount": "350"
#         }}
#     }
#     if request.method == 'POST':
#         test = request.get_json()
#         name = test.get('info').get('name')
#         mail = test.get('info').get('mail')
#         categoryList = list(test.get('moves').keys())
#         print(name)
#         print(mail)
#         print(categoryList)
#         # print(type(test))
#         return (render_template('home.html', nombre=name, mail=mail, categoryList=categoryList))
#     else:
#         return (render_template('home.html', nombre=user, mail='mailtest@gmail.com', today=d2, month_ago=d2, movesList=movesList))


if __name__ == "__main__":
    app.run(debug=True)
