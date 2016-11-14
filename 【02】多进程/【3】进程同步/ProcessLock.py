import multiprocessing
import sys
import random
import time


def write_q(q, lock):
    # 在多进程写入时可以独占共享资源
    lock.acquire()
    for value in ['A', 'B', 'C']:
        print('Put {} to queue...'.format(value))
        q.put(value)
        time.sleep(2)
    lock.release()


def read_q(q):
    while True:
        if not q.empty():
            value = q.get(False)
            print("Get {} from queue".format(value))
        else:
            time.sleep(1)


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    q = multiprocessing.Queue()
    w = multiprocessing.Process(target=write_q, args=(q, lock))
    w2 = multiprocessing.Process(target=write_q, args=(q, lock))
    r = multiprocessing.Process(target=read_q, args=(q,))
    r.start()
    w.start()
    w2.start()
    w.join()
    w2.join()
    r.join()
    print("over")
