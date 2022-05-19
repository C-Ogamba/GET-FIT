from app.forms import RegisterForm,Login
import email
from app import app, db
from flask import redirect, render_template, request, url_for, flash
from .forms import productForm
from app.models import User
from flask_login import current_user
from flask_login import logout_user, login_user



# julie route

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')



# lee route

@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(f'Invalid username or password', 'danger')
            return redirect(url_for('login'))
        # login_user(user, remember=form.remember.data)
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)



# @app.route('/register',methods=['GET','POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = RegisterForm()
#     if form.validate_on_submit():
    
#         user = User(username=form.username.data,email=form.email.data)
#         db.session.add(user)
#         db.session.commit()
    
#         return redirect(url_for('home'))
#     return render_template('register.html',form= form)

@app.route('/trial', methods=['POST', 'GET'])
def trial():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account succesfully created', 'success')
        return redirect(url_for('login'))
        

    return render_template('trial.html',form=form)




# mary and mercy route

@app.route('/products')
def products():
    form=productForm()
    return render_template('products.html', form=form)

# oscar route

@app.route('/user')
def user():
    return render_template('user.html')





