# import time,threading

# #new thread 
# def loop():
# 	print 'thread %s is running...'%threading.current_thread().name
# 	n = 0
# 	while n<5:
# 		n = n+1
# 		print 'thread %s >>> %s'%(threading.current_thread().name,n)
# 		time.sleep(1)
# 		print 'thread %s is ended.'%threading.current_thread().name

# print 'thread %s is running...' %threading.current_thread().name
# t = threading.Thread(target=loop,name = 'LoopThread')
# t.start()
# t.join()
# print 'thread %s ended.'% threading.current_thread().name


# import time,threading

# balance = 0

# #change balance
# def change_it(n):
# 	global balance
# 	balance = balance + n
# 	balance = balance - n
# # #no lock
# # def run_thread(n):
# # 	for i in range(100000):
# # 		change_it(n)
# #thread lock
# lock = threading.Lock()
# def run_thread(n):
# 	for i in range(100000):
# 		#get lock
# 		lock.acquire()
# 		try:
# 			change_it(n)
# 		finally:
# 			lock.release()

# t1 = threading.Thread(target=run_thread,args=(5,))
# t2 = threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print balance

# import threading,multiprocessing

# def loop():
# 	x = 0
# 	while True:
# 		x = x^1
# for i  in range(multiprocessing.cpu_count()):
# 	t = threading.Thread(target=loop)
# 	t.start()


#thread local
import threading

#create global ThreadLocal object
local_school = threading.local()

def process_student():
	print 'Hello,%s (in %s)'%(local_school.student,threading.current_thread().name)

def process_thread(name):
	local_school.student = name
	process_student()

t1 = threading.Thread(target = process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target = process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

