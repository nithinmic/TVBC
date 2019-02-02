def fib(n):
	if n==0 or n==1:
		return 1
	elif n==2:
		return 2
	elif n==3:
		return 3
	else:
		return fib(n-1) + fib (n-2)
print(fib(5))