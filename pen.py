class pen:
	def __init__(self,color,length,meterial):
		self.color = color
		self.length =length
		self.meterial = meterial
	def change_color(self,color):
		self.color=color
	def add_length(self,cap_length):
		self.length+=cap_length
	def __add__(self,other):
		return pen(self.color,self.length+other.length,other.meterial)
# rynolds=pen('black',25,'plastic')
# parker=pen('White',30,'Steel')

# print("Rynolds")
# print("=================")
# print(rynolds.color)
# print(rynolds.length)
# print(rynolds.meterial)
# print("=================")
# print()
# print("Parker")
# print("=================")
# print(parker.color)
# print(parker.length)
# print(parker.meterial)
# print("=================")
# print()
# rynolds.change_color('gray')
# print("Rynolds change_color")
# print("=================")
# print(rynolds.color)
# print(rynolds.length)
# print(rynolds.meterial)
# print("=================")
# print()
# rynolds.add_length(2)
# print("Rynolds add_length")
# print("=================")
# print(rynolds.color)
# print(rynolds.length)
# print(rynolds.meterial)
# print("=================")
# print()
# camel=rynolds+parker
# print("Camel by adding both pen")
# print("=================")
# print(camel.color)
# print(camel.length)
# print(camel.meterial)
# print("=================")
# print()


