def fib_eff(n,d):
	if n in d:
		return d[n]
	else:
		ans= fib_eff(n-1,d)+fib_eff(n-2,d)
		d[n]=ans
		return ans
d={1:1,2:2,3:3,4:5,5:8}
print (fib_eff(1004,d))