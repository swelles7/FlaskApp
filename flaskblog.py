from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 
from forms import RegistrationForm, LoginForm
from models import User, Post 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



posts = [
	{
	'author': 'Steven Welles',
	'title': 'Blog 1',
	'content': 'A lot of info',
	'date_posted': 'April 22, 2018'
	},
	{
	'author': 'Jane Welles',
	'title': 'Blog 2',
	'content': 'A little of info',
	'date_posted': 'April 23, 2018'
	}


]



@app.route("/")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
			flash(f'Account created for {form.username.data}!', 'success')
			return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
	app.run(debug=True)


