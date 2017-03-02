#master/worker 

#taskmanager.py
import random,time,Queue
from multiprocessing.managers import BaseManager

#send queue
task_queue = Queue.Queue()
#receive queue
result_queue = Queue.Queue()

#from BaseManager inherit QueueManager
class QueueManager(BaseManager):
	pass

#register two queue to network
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)

#
manger = QueueManager(address=('',5000),authkey='abc')
manger.start()

task = manger.get_task_queue()
result = manger.get_result_queue()

#add tasks
for i in range(10):
	n = rangdom.randint(0,10000)
	print('Put task %d...'%n)
	task.put(n)

#get results
print('Try get result')
for i in range(10):
	r = result.get(timeout=10)
	print('Result:%s'%r)
#close
manager.shutdown()


#taskworker.py
import time.sys.Queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('Connect to server %s...'%server_addr)
m = QueueManager(address=(server_addr,5000),authkey='abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
	try:
		n = task.get(timeout=1)
		print('run task %d*%d...'%(n,n))
		r = '%d*%d = %d'%(n,n,n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty')
#end
print('worker exit.')