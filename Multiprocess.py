
# #use fork for multiprocess
# import os

# print 'Process (%s) start...'%os.getpid()

# pid = os.fork()

# if pid == 0:
# 	print 'I am child process (%s) and my parent is %s.'%(os.getpid(),os.getppid())
# else:
# 	print 'I (%s) just created a child process (%s).'%(os.getpid(),pid)

# #use mutiprocessing module for mutiprocess
# from multiprocessing import Process
# import os

# #child process 
# def run_proc(name):
# 	print 'Run child process %s (%s)...'%(name,os.getpid())

# if __name__ == '__main__':
# 	print "Parent process %s."%os.getpid()
# 	p = Process(target=run_proc,args=('test',))
# 	print 'Process will start.'
# 	p.start()
# 	p.join() # this function is just for wait the process end
# 	print 'Process end.'


# #use pool
# from multiprocessing import Pool
# import os,time,random

# def long_time_task(name):
# 	print 'Run task %s (%s)...'%(name,os.getpid())
# 	start = time.time()
# 	time.sleep(random.random()*3)
# 	end = time.time()
# 	print 'Task %s runs %0.2f seconds.' %(name,(end-start))

# if __name__ == '__main__':
# 	print 'Parent process %s.' %os.getpid()
# 	p = Pool()
# 	for i in range(5):
# 		p.apply_async(long_time_task,args=(i,))
# 	print 'Waintng for all subprocesses done...'
# 	p.close()
# 	p.join()
# 	print 'All subprocesses done.'

#multiprocess communicate

from multiprocessing import Process,Queue
import os,time,random

#write data
def write(q):
	for value in ['A','B','C']:
		print 'Put %s to queue...'%value
		q.put(value)
		time.sleep(random.random())
#read data
def read(q):
	while True:
		value = q.get(True)
		print 'Get %s from queue.'%value
if __name__ == '__main__':
	#parent process create queue and put it to other child process.
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	#start child process pw
	pw.start()
	#start child process pr
	pr.start()
	#wait for pw goto end
	pw.join()
	#pr process is a dead circule, it can't be wait for end, so must force to end it
	pr.terminate()
	
