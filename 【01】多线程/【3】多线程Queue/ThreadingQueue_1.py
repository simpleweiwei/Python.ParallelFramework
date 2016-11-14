import queue  # Python 2 中的Queue模块在Python 3中更名为 queue
import threading
import time

"""
queue主要用于线程间的通信，自带同步功能（enqueue和dequeue不用手动加锁）

Q.task_done()表示一个任务（例如一个dequeue的元素）已经结束

Q.join()为等待队列为空才退出程序
"""
# 队列FIFO
queue = queue.Queue()


class ThreadNum(threading.Thread):
    """每打印一个数字等待1秒，并发打印10个数字需要多少秒？"""

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # 消费者端，从队列中获取num
            num = self.queue.get()
            print("输出：I'm num {}".format(num))
            time.sleep(1)
            # 在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号
            self.queue.task_done()


start = time.time()


def main():
    # 产生一个 threads pool, 并把消息传递给thread函数进行处理，这里开启10个并发
    for i in range(10):
        t = ThreadNum(queue)
        t.daemon = True
        t.start()

    # 往队列中填充数据
    for num in range(10):
        queue.put(num)
        print("输入： " + str(num))
    # wait on the queue until everything has been processed
    queue.join()

if __name__ == '__main__':
    main()
    print("Elapsed Time: {}".format(time.time() - start))

"""
备注：

1 FIFO队列先进先出：class Queue.Queue(maxsize)
2 LIFO类似于堆,即先进后出：class Queue.LifoQueue(maxsize)
3 优先级队列级别越低越先出来：class Queue.PriorityQueue(maxsize)
"""