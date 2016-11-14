import threading
import time

# 同时最多有2个线程可以获得semaphore（锁），用来控制对共享资源的调用

semaphore = threading.Semaphore(2)


def func():
    if semaphore.acquire():
        for i in range(2):
            print(threading.currentThread().getName() + ' get semaphore')
        semaphore.release()
        print(threading.currentThread().getName() + ' release semaphore')


for i in range(10):
    t1 = threading.Thread(target=func)
    t1.start()