from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/info/<user>')
def info(user):
    return "Hello: " + user


@app.route('/post/<post_id>')
def post(post_id):
    return "Post Number: " + post_id


if __name__ == "__main__":
    app.run(debug=True)