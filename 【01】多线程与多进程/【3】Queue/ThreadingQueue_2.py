import queue as Q
import threading
import time

# 一个队列的输出可以作为另一个队列的输入
queue = Q.Queue()
out_queue = Q.Queue()


class ThreadNum(threading.Thread):
    def __init__(self, queue, out_queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while True:
            # 从队列中取消息
            num = self.queue.get()
            bkeep = num
            # 将bkeep放入队列中
            self.out_queue.put(bkeep)
            # signals to queue job is done
            self.queue.task_done()


class PrintLove(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, out_queue):
        threading.Thread.__init__(self)
        self.out_queue = out_queue

    def run(self):
        while True:
            # 从队列中获取消息并赋值给bkeep
            bkeep = self.out_queue.get()
            keke = "I love " + str(bkeep)
            print(keke),
            print(self.getName())
            time.sleep(1)
            # signals to queue job is done
            self.out_queue.task_done()


start = time.time()


def main():
    # populate queue with data
    for num in range(10):
        queue.put(num)

    # spawn a pool of threads, and pass them queue instance
    for i in range(5):
        t = ThreadNum(queue, out_queue)
        t.setDaemon(True)
        t.start()
    for i in range(5):
        pl = PrintLove(out_queue)
        pl.setDaemon(True)
        pl.start()
    # wait on the queue until everything has been processed
    queue.join()
    out_queue.join()


if __name__ == '__main__':
    main()
    print("Elapsed Time: {}".format(time.time() - start))
