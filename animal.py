class Animal(object):
	def __init__(self, name,age,hight,weight,color):
		self.age = age
		self.name=name
		self.hight=hight
		self.weight=weight
		self.color=color
	def set_name(self,newname=""):
		self.name=newname
	def set_age(self,newage):
		self.age=newage
	def set_hight(self,newhight):
		self.hight=newhight
	def set_weight(self,newweight):
		self.weight=newweight
	def set_color(self,newcolor):
		self.color=newcolor
	def get_name(self):
		return self.name
	def get_age(self):
		return self.age
	def get_hight(self):
		return self.hight
	def get_weight(self):
		return self.weight
	def get_color(self):
		return self.color
	def __str__(self):
		return "Animal: "+str(self.name)+":"+str(self.age)+":"+str(self.hight)+":"+str(self.weight)+":"+str(self.color)
# jimmy=Animal(10)
# print (jimmy.age,jimmy.name)
# jimmy.set_name("tony")
# print (jimmy.age,jimmy.name)
# print(jimmy.get_name())
# print(jimmy.get_age())
# jimmy.set_age(45)
# print (jimmy.age,jimmy.name)