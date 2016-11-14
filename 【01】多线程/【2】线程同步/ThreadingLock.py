import threading
import time

# 利用锁进行同步
# 如不同步，则list可能为[1, 4, 4, 7, 7, 8]
# 如同步，则list为[1, 2, 4, 6, 7, 8]是有序添加
my_count = 0
list =[]


class MyThread(threading.Thread):
    def __init__(self, func, add_value, times, thread_name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.add_value = add_value
        self.times = times
        self.name = thread_name

    def run(self):
        self.func(self.add_value, self.times, self.name)  # 不要用哪个apply函数，已经废弃了


def add(add_value, times, name):
    global my_count
    global list
    for i in range(times):
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        my_count += add_value
        print("Threading {} value: {}".format(name, my_count))
        list.append(my_count)
        # 释放锁
        threadLock.release()
        # time.sleep(random.randint(1, 3))

len = 3  # 启动3个线程
threads = []
t1 = MyThread(add, 1, 2, "Threading" + str(1))
threads.append(t1)
t2 = MyThread(add, 2, 2, "Threading" + str(2))
threads.append(t2)
t3 = MyThread(add, 1, 2, "Threading" + str(3))
threads.append(t3)
threadLock = threading.Lock()

if __name__ == '__main__':
    for j in range(len):
        threads[j].daemon = True
        threads[j].start()
    for j in range(len):
        threads[j].join()
    print("all over at {}".format(time.ctime()))
    print(my_count)
    print(list)
