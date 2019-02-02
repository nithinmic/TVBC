from animal import Animal

class Person(Animal):
	def __init__(self,name,age,hight,weight,color,university,job,school):
		Animal.__init__(self,name,age,hight,weight,color)
		self.university=university
		self.job=job
		self.school=school
		self.friends=[]
	def get_friends(self):
		return self.friends
	def add_friend(self,fname):
		self.friends.append(fname)
	def age_diff(self,other):
		diff=self.age-other.age
	def __str__(self):
		return "Person: "+str(self.name)+":"+str(self.age)+":"+str(self.hight)+":"+str(self.weight)+":"+str(self.color)+":"+str(self.university)+":"+str(self.job)+":"+str(self.school)
# nithin=Person("nithin",25,177,85,"brown","Madras university","JPMC","St.Anonys")
# print(nithin)