from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/profile')
def profile():
    return 'Profile'

if __name__ == '__main__':
    app.run()