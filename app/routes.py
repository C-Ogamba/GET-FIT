from app import app
from flask import render_template 
from .forms import productForm


# julie route

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')



# lee route

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/reg')
def reg():
    return render_template('register.html')



# mary and mercy route

@app.route('/products')
def products():
    form=productForm()
    return render_template('products.html', form=form)

# oscar route

@app.route('/user')
def user():
    return render_template('user.html')





