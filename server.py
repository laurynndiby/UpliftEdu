from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'upliftedu'

@app.route('/')
def home():
    return 'Hello World'

@app.route('/profile/<int:profile_id>')
def profile(profile_id):
    return 'Profile number: ' + str(profile_id)

if __name__ == '__main__':
    app.run()

