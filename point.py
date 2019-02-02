class point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self):
		return "({},{})".format(self.x,self.y)
	def __add__(self,other):
		return point(self.x+other.x,self.y+other.y)
	def distance(self,other):
		x_diff=(self.x-other.x)**2
		y_diff=(self.y-other.y)**2
		return (x_diff+y_diff)**0.5

# a=point(5,6)
# b=point(7,8)
# print(a+b)
# print(a)
# print(a.distance(b))
# print(point.distance(a,b))
