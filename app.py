from flask import Flask, render_template #, flash, redirect, url_for, session, request, logging
from data import Articles
#from flask_sqlalchemy
#from wtforms import Form, StringField, Loginform, PasswordField, validators


app = Flask(__name__)
#app.config['SECRET_KEY'] ='asdf'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://website.db'
#db = SQLAlchemy(app)

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

#class RegisterForm(Form):
    #name = StringField('Name', [validators.Length(min=1, max=50)])
    #username=StringField('Username', [validators.Length(min=4, max=25)])
    #email = StringField('Email', [validators.Length(min=6, max=50)])
    #password = PasswordField('Password', [
        #validators.DataRequired().
        #validators.EqualTo('confirm', message = 'Passwords do not match')
    #])
    #confirm = PasswordField('Confirm Password')

#@app.route('/register', methods=['GET', 'POST'])
#def register():
    #form = RegisterForm(request.form)
    #if request.method == 'POST' and  form.validate():
        #return render_template('register.html', form=form)

if __name__=='__main__':
    app.run(debug=True)

