import threading  # 不要用老的thread
import time
# 基本调用

def music(*func):
    for i in range(2):
        print("I was listening to {} at {}".format(func, time.ctime()))
        time.sleep(1)


def movie(*func):
    for i in range(2):
        print("I was watching the movie {} at {}".format(func, time.ctime()))
        time.sleep(5)


threads = []
t1 = threading.Thread(target=music, args=r'爱情买卖')
threads.append(t1)
t2 = threading.Thread(target=movie, args=r'阿凡达')
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.daemon = True  # 设为守护线程
        t.start()
        t.join()
    print("all over at {}".format(time.ctime()))
