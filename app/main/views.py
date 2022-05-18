from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from . forms import AddActivity
from flask.views import View,MethodView


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'GetFit'
    return render_template('index.html', title = title)

@main.route('/categories')
def categories():
    title = 'GetFit | Categories'
    GetFit = GetFit.query.filter_by().first()
    bodybuilding = GetFit.query.filter_by(category="bodybuilding")
    sportdances = GetFit.query.filter_by(category = "sportdances")
    
    return render_template('categories.html',title =title, GetFit = GetFit, bodybuilding=bodybuilding, sportdances=sportdances,)

@main.route('/trainer/new/<int:trainer_id>', methods = ['GET','POST'])
def new_trainer(class_id):
    form = TrainerForm()
    activity=Class.query.get(class_id)
    if form.validate_on_submit():
        description = form.description.data
        new_trainer=Trainer(description = description, user_id = current_user._get_current_object().id, class_id = class_id)
        db.session.add(new_trainer)
        db.session.commit()
        return redirect(url_for('.new_trainer', class_id= class_id))
    
    @main.route('/prices')
    def prices():
        title = 'GetFit | Prices'
    GetFit = GetFit.query.filter_by().first()
    basic = GetFit.query.filter_by(category="basic")
    unlimited = GetFit.query.filter_by(category = "unlimited")
    
    return render_template('price.html',title =title, GetFit = GetFit, basic=basic, unlimited=unlimited,)
