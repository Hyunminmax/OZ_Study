from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "it's 몸살"

    return userlist

@app.route('/about')
def about():
    return "몸살 is too bad."

if __name__ == '__main__':
    app.run()

