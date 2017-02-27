import functools

#this function is to change sting to int in binary sysytem
int2 = functools.partial(int,base=2)

if __name__ == '__main__':
	#the result is decimal system
	print int2("1000000")

