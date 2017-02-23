

#define a function for get absolute value with int or float
def my_abs(*x):
	if isinstance(x,tuple):
		x = list(x)
		for index,e in enumerate(x):
			if isinstance(e,(int,float)):
				if e<0:
					x[index] = -e
	else:
		return None

	if len(x) == 1:
		return x[0]
	else:
		return x
		

if __name__ == '__main__':
	print my_abs(None)
	#get absolute value for int type
	print my_abs(3)
	#get absolute value for float type
	print my_abs(-1.2)
	#get absolute value for string
	print my_abs("a")
	#get asolute value for list
	print my_abs([1,2])
	#get absolute value for two int type parameters
	print my_abs(1,-2)
	#get  absolute value for two parameters,an int type and a string type
	print my_abs(-1,'a')
