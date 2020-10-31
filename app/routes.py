from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm
from app.models import Sunshine
#from db import get_db


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

"""
@app.route('/sunshine')
def test():
    db = get_db()
    cur = db.execute('select * from sunshine where id=1')
    emails = cur.fetchall()
    print(emails)
    return render_template('report.html', emails=emails) #name=links,
"""
@app.route('/sunshine')
def test():
    #db = get_db()
    #cur = db.execute('select * from sunshine where id=1')
    #emails = cur.fetchall()
    #print(emails)
    #query = Sunshine.query.order_by(Sunshine.salary.desc())#.one()
    #query = Sunshine.query.one()
    query = Sunshine.query('salary').one()
    return render_template('sunshine.html', query=query) #name=links, emails=emails
