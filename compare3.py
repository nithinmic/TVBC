a= input('Enter a number: ')
b= input('Enter a second number: ')
c= input('Enter the third number: ')

def compare(x,y):
		if x>y:
			return x 
		elif x<y:
			return y

try:
 	int(a)
 	int(b)
 	int(c)
 	print('the Greatest Number is',compare(c,compare(a,b)))

except:
	print('Invalid Input!!!!!!!  Please only enter numbers')

