
#add log function to a function
def log(func):
	def wrapper(*args,**kw):
		print 'call %s():'%func.__name__
		return func(*args,**kw)
	return wrapper

#if you want to transform some parameter
def log2(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print "%s %s():"% (text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator


import functools
def log3(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call %s()'%func.__name__
		return func(*args,**kw)
	return wrapper

def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log
def now():
	print '2013-12-25'

@log2('execute')
def now2():
	print '2013-12-25'

@log3
def now3():
	print '2013-12-25'

@log4('execute')
def now4():
	print '2013-12-25'


if __name__ == '__main__':
	now()
	now2()
	now3()
	now4()