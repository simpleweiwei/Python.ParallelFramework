import multiprocessing
import time

"""
Semaphore管理一个内置的计数器，
每当调用acquire()时内置计数器-1；
调用release() 时内置计数器+1；
计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。
"""


# 使用信号量控制进程个数

# Semaphore用来控制访问共享资源的进程数量

# Semaphore 相当于 N 把锁，获取其中一把就可以执行了。信号量的总数 N 在构造时传入，s = Semaphore(N)。

# 例如multiprocessing.Semaphore(2)代表最多有两把锁，也就是说最多有两个进程同时访问共享资源
def worker(s, i):
    s.acquire()
    print(multiprocessing.current_process().name + " acquire")
    time.sleep(i)
    print(multiprocessing.current_process().name + " release")
    s.release()


if __name__ == "__main__":
    s = multiprocessing.Semaphore(2)
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(s, i * 2))
        p.start()
