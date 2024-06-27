from app import app
from flask import render_template
from app.forms import LoginForm, RegisterForm, AddProductForm
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route('/Home')
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/about-me')
def about_me():
    """About Me URL"""
    return render_template('about_me.html', title='About Me Page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You are requesting to register as {form.username.data}')
        return redirect( url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login URL"""
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'You are requesting to login as {form.username.data}')
        return redirect( url_for('index'))
    return render_template('login.html', title='Login', form=form)


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """Add Product URL"""
    form = AddProductForm()
    if form.validate_on_submit():
        flash('You are requesting to add a product')
        return redirect( url_for('add_product'))
    return render_template('add_product.html', title='Add Product', form=form)








