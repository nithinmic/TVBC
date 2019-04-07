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

@app.route("/signuppage")
def signuppage():
	return render_template('signup.html')

@app.route("/login", methods =['GET','POST'])
def login():
	if request.method=='POST':
		uname=request.form['username']
		pwd=request.form['password']
		if check_user(uname):
			result=log_user(uname)
			if pwd==result['pwd']:
				session['username']=result['username']
				session['type']=result['ctype']
				return redirect(url_for('home'))
			return "Please enter correct password!"
		return "User dosn't exist!"

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
		if user_info['ctype'] == 'buyer':
			user_info['cart']={}
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

@app.route('/add_products', methods= ['GET','POST'])
def add_products():
	if request.method =='POST':
		product_info={}
		product_info['pname']=request.form['pname']
		product_info['pdescription']=request.form['pdescription']
		product_info['pprice']=int(request.form['pprice'])
		product_info['sellername']=session['username']

		if check_product(product_info['pname']):
			return "product Already exist"
		create_product(product_info)
		return redirect(url_for('home'))
	return render_template('add_products.html')

@app.route('/remove_product', methods= ['GET','POST'])
def remove_products():
	product_id=request.form['product_id']
	remove_product(product_id)
	return redirect(url_for('seller_products'))

@app.route('/buyer_products')
def b_products():
	products=buyer_products()
	return render_template('products.html',products=products)

@app.route('/seller_products')
def sell_products():
	products=seller_products(session['username'])
	return render_template('products.html',products=products)

@app.route('/add_cart', methods=['POST'])
def add_tocart():
	product_id=request.form['product_id']
	update_cart(product_id,session['username'])
	return redirect(url_for('cart'))

@app.route("/cart")
def cart():
	# import pdb; pdb.set_trace()
	products=cart_page(session['username'])
	return render_template('cart_page.html',products=products)

@app.route('/remove_cart',methods=['POST'])
def remove_cart():
    product_id=request.form['product_id']
    remove_from_cart(session['username'],product_id)
    return(redirect(url_for('cart')))

app.run(debug=True)