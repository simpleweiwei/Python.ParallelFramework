import threading
import time

"""
Event实现与Condition类似的功能，不过比Condition简单一点。它通过维护内部的标识符来实现线程间的同步问题。

使用threading.Event可以使一个线程等待其他线程的通知，我们把这个Event传递到线程对象中，Event默认内置了一个标志，初始值为False。
一旦该线程通过wait()方法进入等待状态，直到另一个线程调用该Event的set()方法将内置标志设置为True时，该Event会通知所有等待状态的线程恢复运行。
"""


class MyThread(threading.Thread):
    def __init__(self, signal):
        threading.Thread.__init__(self)
        self.singal = signal

    def run(self):
        print("I am {},I will sleep ...".format(self.name))
        self.singal.wait()
        print("I am {},I awake ...".format(self.name))


if __name__ == "__main__":
    singal = threading.Event()
    for t in range(0, 3):
        thread = MyThread(singal)
        thread.start()

    print("main thread sleep 3 seconds... ")
    time.sleep(3)

    singal.set()
