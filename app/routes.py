from flask import render_template, flash, redirect, url_for, jsonify
from app import app, db
from app.forms import LoginForm
from app.models import Sunshine
from sqlalchemy import func
import json


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

@app.route('/sunshine')
def graph():
    #query = Sunshine.query.order_by(Sunshine.id.desc()) #.one()
    #query = Sunshine.query.all()
    #query = Sunshine.query.filter(Sunshine.first_name == 'david')
    #query = Sunshine.query.with_entities(Sunshine.first_name).filter(Sunshine.first_name.ilike("david")).all()
    query = 3 #delete, this is throw away variable
    """
    query = Sunshine.query.filter(Sunshine.first_name.ilike("david")).all()
    results = [
        {
            "id": person.id,
            "sector": person.sector,
            "last_name": person.last_name,
            "first_name": person.first_name,
            "salary": person.salary,
            "taxable": person.taxable,
            "employer": person.employer,
            "job_title": person.job_title,
            "calendar_year": person.calendar_year
        } for person in query
    ]
    """
    #query = Sunshine.query.one()
    #query = Sunshine.query('salary').one()
    """
    engine = create_engine('postgresql://postgres:PoBuCe60@localhost:5432/statscan')
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Sunshine.first_name).order_by(Sunshine.first_name)
    """
    return render_template('sunshine.html') #query=jsonify(results) OR query=map(json.dumps,results)
    #return {"count": len(results), "Person": results[0]}

@app.route('/data')
def sunshinedata():
    query = Sunshine.query.filter(Sunshine.first_name.ilike("david")).all()
    results = [
        {
            "id": person.id,
            "sector": person.sector,
            "last_name": person.last_name,
            "first_name": person.first_name,
            "salary": person.salary,
            "taxable": person.taxable,
            "employer": person.employer,
            "job_title": person.job_title,
            "calendar_year": person.calendar_year
        } for person in query
    ]
    return jsonify(results)
