from multiprocessing import JoinableQueue, Process
import time

"""
强化版本的 JoinableQueue, 新增两个方法 task_done() 和 join()。
task_done() 是给消费者使用的，每完成队列中的一个任务，调用一次该方法。
当所有的 tasks 都完成之后，交给调用 join() 的进程执行。
"""
def consumer(q):
    while True:
        print("consumer", q.get())
        q.task_done()


jobs = JoinableQueue()

for i in range(10):
    jobs.put(i)

for i in range(10):
    p = Process(target=consumer, args=(jobs,))
    p.daemon = True # 如果不调用的话主进程结束，子进程依然不会结束
    p.start()

jobs.join() # 这个 join 函数等待 JoinableQueue 为空的时候，等待就结束，可以执行下面的东东
print("over")
