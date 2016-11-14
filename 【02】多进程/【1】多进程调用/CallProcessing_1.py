from multiprocessing import Process,current_process
import os
import time
import random


# 多进程可以规避GIL的坑，充分利用机器多处理器的优势，核越多性能越好
# python多进程调用（multiprocessing调用多进程可以跨平台）
# 进程可以起名字
# 结束一个进程可以调用它的 terminate() 方法
def my_double(number):
    result = number * 2
    pid = os.getpid()  # get process id
    pname = current_process().name  # get process name
    time.sleep(random.randint(1, 5))
    print("{0} doubled to {1} by process id: {2} name: {3}".format(number, result, pid, pname))


if __name__ == '__main__':
    numbers = ['1', '5', '9', '4', '6']
    procs = []
    for index, value in enumerate(numbers):
        proc = Process(target=my_double, name="process" + str(index), args=value)
        proc.daemon = True  # 主进程结束，子进程就结束了
        procs.append(proc)
        proc.start()
    for p in procs:
        p.join()

    print("over")
