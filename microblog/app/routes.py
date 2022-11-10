from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    # mockup user
    user = {'username': 'Civix'}
    posts = [
        {
            'author': {'username': 'Jonh'},
            'body': 'Very long post of Jonh :D'
        },
        {
            'author': {'username': 'Me'},
            'body': 'Gintama the movie 2 is so cool :D'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login request for user {form.username.data}, rememeber me={form.remember_me.data}')
        return redirect(url_for(index))
    return render_template('login.html', title='Sign in', form=form)