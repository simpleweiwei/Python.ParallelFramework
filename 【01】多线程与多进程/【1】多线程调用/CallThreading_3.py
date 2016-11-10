import threading
from time import sleep, ctime
# 不推荐此种调用方式
loops = [4, 2]


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(self.args)


def loop(args):
    print("start loop {} at: {}".format(args[0], ctime()))
    sleep(args[1])
    print("loop {} done at: {}".format(args[0], ctime()))


def main():
    print("starting at: {}".format(ctime()))
    threads = []
    nloops = range(len(loops))

    for i in nloops:  # create all threads
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:  # start all threads
        threads[i].start()

    for i in nloops:  # wait for completion
        threads[i].join()
    print("all DONE at: {}".format(ctime()))


if __name__ == '__main__':
    main()
