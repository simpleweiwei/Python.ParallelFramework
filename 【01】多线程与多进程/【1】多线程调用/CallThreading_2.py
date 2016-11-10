import threading
import time
# 创建自己的线程类

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def get_result(self):
        return self.res

    def run(self):
        self.res = self.func(self.args)  # 不要用哪个apply函数，已经废弃了


def play(args):
    for i in range(2):
        print("Start playing:{} at {}".format(args[0], time.ctime()))
        time.sleep(args[1])



list = {'PPAP.mp3': 3, 'Hero.mp4': 5}
threads = []
for k, v in list.items():
    t = MyThread(play, (k, v), play.__name__)
    threads.append(t)

if __name__ == '__main__':
    loop_list = range(len(list))
    for j in loop_list:
        threads[j].daemon = True
        threads[j].start()
    for j in loop_list:
        threads[j].join()
    print("all over at {}".format(time.ctime()))
