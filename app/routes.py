import email
from app import app, db
from flask import redirect, render_template, request, url_for 
from .forms import productForm
from app.models import User



# julie route

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')



# lee route

@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/reg', methods=['POST', 'GET'])
def reg():
    if request.method=='POST':
        # user=User(username=request.form.get('name'), email=request.form.get('email'), password=request.form.get('pass'))
        # db.session.add(user)
        # db.session.commit()
        user=request.form.get('name')
        print(user, 'worked')
        return  redirect(url_for('login'))
    print("invalid request")
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





