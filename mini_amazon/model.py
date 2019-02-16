from pymongo import MongoClient

client = MongoClient()
db=client['mini_amazon']
def check_user(username):
	query={"username":username}
	results=db['users'].find(query)

	if results.count()>0:
		return True
	return False
def create_user(user_info):
	db['users'].insert_one(user_info)
	
def log_user(username):
	query={"username":username}
	results=db['users'].find_one(query)
	return results

def check_product(pname):
	query={"pname":pname}
	results=db['products'].find(query)

	if results.count()>0:
		return True
	return False
def create_product(product_info):
	db['products'].insert_one(product_info)

def buyer_products():
	results=db['products'].find({})
	return results

def seller_products(seller):
	query={"sellername":seller}
	results=db['products'].find(query)
	return results


def update_cart(product_id,username):
	query={"username":username}
	results=db['users'].find_one(query)
	if results.get(cart):
		db.['users'].update( { "username":username}, { "$addToSet" : { cart: {"$each":[product_id]}}})
	else:
		db.['users'].update( { "username":username}, { "$set" : { cart: product_id}})
	return results