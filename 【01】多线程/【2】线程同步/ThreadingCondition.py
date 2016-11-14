import threading
import time

"""
Python提供的Condition对象提供了对复杂线程同步问题的支持。

Condition被称为条件变量，除了提供与Lock类似的acquire和release方法外，还提供了wait和notify方法。

使用Condition的主要方式为：线程首先acquire一个条件变量，然后判断一些条件。如果条件不满足则wait；如果条件满足，进行一些处理改变条件后，通过notify方法通知其他线程，其他处于wait状态的线程接到通知后会重新判断条件。不断的重复这一过程，从而解决复杂的同步问题。

下面我们通过很著名的“生产者-消费者”模型来来演示下，在Python中使用Condition实现复杂同步。

代码中主要实现了生产者和消费者线程，双方将会围绕products来产生同步问题，首先是2个生成者生产products ，而接下来的10个消费者将会消耗products
"""
condition = threading.Condition()
products = 0


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, products
        while True:
            if condition.acquire():
                if products < 10:
                    products += 1
                    print("Producer {}:生产一个, 现在products为:{}".format(self.name, products))
                    condition.notify()
                else:
                    print("Producer {}:已经为 10, 停止生产, 现在products为:{}".format(self.name, products))
                    condition.wait()
                condition.release()
                time.sleep(2)


class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, products
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print("Consumer {}:消费一个, 现在products为:{}".format(self.name, products))
                    condition.notify()
                else:
                    print("Consumer {}:只有一个, 停止消费，现在products为:{}".format(self.name, products))
                    condition.wait()
                condition.release()
                time.sleep(2)


if __name__ == "__main__":
    for p in range(0, 2):
        p = Producer()
        p.start()

    for c in range(0, 10):
        c = Consumer()
        c.start()

"""
另外：
Condition对象的构造函数可以接受一个Lock/RLock对象作为参数，如果没有指定，则Condition对象会在内部自行创建一个RLock；
除了notify方法外，Condition对象还提供了notifyAll方法，可以通知waiting池中的所有线程尝试acquire内部锁。
由于上述机制，处于waiting状态的线程只能通过notify方法唤醒，所以notifyAll的作用在于防止有线程永远处于沉默状态。
"""
