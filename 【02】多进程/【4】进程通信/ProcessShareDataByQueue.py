import multiprocessing
from multiprocessing import Queue
import time


# 用queue进行进程通信，只是get和put会阻塞进程，记得加上timeout
# 有一个简化版本的 multiprocessing.queues.SimpleQueue, 只支持3个方法 empty(), get(), put()
def producer(q, num):
    q.put(num)
    print("put %s to q" % num)
    time.sleep(1)


def consumer(q):
    while True:
        try:
            print("consumer", q.get(timeout=5))
        except Exception:
            break


if __name__ == '__main__':
    q = Queue(5)
    for i in range(10):
        p = multiprocessing.Process(target=producer, args=(q, i))
        p.start()
    c = multiprocessing.Process(target=consumer, args=(q,))
    c.start()
    c.join()
    print("Finished")
