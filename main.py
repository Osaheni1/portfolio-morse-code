from flask import Flask, render_template, redirect, url_for, flash, abort, request
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from flask_gravatar import Gravatar
from morse import *
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MorseMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)

db.create_all()


gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)

@app.route('/')
def home():
    coded_message = MorseMessage.query.all()
    print(coded_message)
    i = []
    w = []
    for mes in coded_message:


        i.append(call(mes.message))


    for item in i:
        x = ''.join(item)
        w.append(x)
    print(w)
    return render_template('index.html', res=w)

@app.route('/save_ano', methods=['GET', 'POST'])
def save_ano():
    if request.method == 'POST':
        new_message = MorseMessage(
            message=request.form['message']
        )
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
