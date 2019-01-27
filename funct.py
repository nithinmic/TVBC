a= int(input('Enter a number: '))
b= int(input('Enter a second number: '))

def compare(x,y):
	if x>y:
		return "{0} is greater than {1}".format(x,y)
	elif x<y:
		return "{1} is greater than {0}".format(x,y)
print(compare(a,b))