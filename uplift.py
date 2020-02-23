from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uplift.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    school = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        name1 = request.form['name']
        new_name = Users(name=name1)
        school1 = request.form['school']
        new_school = Users(school=school1)
        try:
            db.session.add(new_name)
            db.session.add(new_school)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your information'
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
