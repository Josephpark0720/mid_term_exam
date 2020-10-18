from flask import Flask, render_template, redirect, url_for, session, request
from flask_bootstrap import Bootstrap
from form import SubmitForm
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random'
bootstrap = Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/sub_form', methods = ['GET', 'POST'])
def sub_form():
    form = SubmitForm()
    if request.method == 'POST':
        return redirect(url_for('board'))
    return render_template('sub_form.html', form=form)

@app.route('/')
def index():
    return redirect('/board')

@app.route('/board')
def board():
    return render_template('board.html')

if __name__ =='__main__':
    app.run()
