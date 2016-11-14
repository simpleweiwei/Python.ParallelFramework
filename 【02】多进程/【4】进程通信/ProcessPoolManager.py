from multiprocessing import Process, Queue, Pool
import multiprocessing
import os, time, random


# 进程池中进程间共享资源必须用Manager
# 当然了如果需要同步用的锁也应该是Manager中的锁


# 写数据进程执行的代码:
def write(q, lock):
    lock.acquire()  # 加上锁
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
    lock.release()  # 释放锁


# 读数据进程执行的代码:
def read(q):
    while True:
        try:
            value = q.get(timeout=5)
        except Exception:
            break
        print('Get %s from queue.' % value)
        time.sleep(random.random())


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    # 父进程创建Queue，并传给各个子进程：
    q = manager.Queue()
    lock = manager.Lock()  # 初始化一把锁
    p = Pool()
    pw = p.apply_async(write, args=(q, lock))
    pr = p.apply_async(read, args=(q,))
    p.close()
    p.join()
    print('所有数据都写入并且读完')
