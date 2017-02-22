
#method one ,define a function for get the result
#get square 
def get_square(num):
	"""
	Summary:
	This function is for get square 
	Args:
	num  the number that for get square
	"""
	return num**2

#make all int or float type square in list 
def get_square_list(l):	
	status = "the list has no changed" 
	for index,e in enumerate(l):
		#check element is int or float type in list
		if isinstance(e,(int,float)):
			l[index]=get_square(e)
			status = "the list has changed"
	return status

if __name__ == '__main__':
	l = [12,2.3,"hello"]
	print get_square_list(l)
	print l