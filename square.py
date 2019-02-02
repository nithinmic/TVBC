from point import point
a=point(0,0)
b=point(0,2)
c=point(2,2)
d=point(2,0)

class square:
	def __init__(self,p1,p2,p3,p4):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.p4 = p4
	def area(self):
		return(self.p1.distance(self.p2))**2
# e=square(a,b,c,d)
# print(e.area())