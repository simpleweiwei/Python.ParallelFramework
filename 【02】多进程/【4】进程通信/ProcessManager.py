from multiprocessing import Process, Manager

"""
Python中还有一统天下的 Server process，专门用来做进程间数据共享。
其支持的类型非常多:
list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Queue, Value 和 Array
"""


# 一个 Manager 对象是一个服务进程，推荐多进程程序中，数据共享就用一个 manager 管理
def func(dct, lst, val):
    dct[1] = 88
    lst.reverse()
    val.value = 3.14


manager = Manager()
dct = manager.dict()
lst = manager.list(range(1, 10))
val = manager.Value('d', 0.0)

p = Process(target=func, args=(dct, lst, val))
p.start()
p.join()
print(dct, '|', lst, '|', val.value)
