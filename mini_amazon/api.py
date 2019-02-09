from flask import Flask, render_template, request,redirect,url_for,session
from model import *
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'hello'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def abt():
	return render_template('about.html')

@app.route("/contact")
def cont():
	return render_template('contacts.html')

@app.route("/login", methods =['GET','POST'])
def login():
	if request.method=='POST':
		nithin={'uname':'nithin','pwd':'12345'}
		uname=request.form['username']
		pwd=request.form['password']
		if nithin['uname']==uname and nithin['pwd']==pwd:
			session['username']=uname
			return redirect(url_for('home'))
		else:
			return redirect(url_for('home'))
	else:
		return redirect(url_for('home'))

@app.route('/signup', methods =['GET','POST'])
def signup():
	if request.method=='POST':

		user_info={}

		user_info['username']=request.form['username']
		user_info['email']=request.form['email']
		user_info['pwd']=request.form['password']
		rpwd=request.form['password2']
		user_info['ctype']=request.form['ctype']
		if check_user(user_info['username']) is False:
			if rpwd==user_info['pwd']:
				create_user(user_info)
			else:
				return "Passwords dons't match! Retry"
		else:
			return "User id already exist!"
	return redirect(url_for('home'))

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('home'))

app.run(debug=True)