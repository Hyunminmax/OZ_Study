from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'username': 'traveler', 'name': 'Alex'},
        {'username': 'photograher', 'name': 'Sam'},
        {'username': 'gourmet', 'name': 'Chris'}
    ]
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run()