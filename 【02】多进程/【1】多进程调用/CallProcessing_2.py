import multiprocessing
import time
import os


class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("process {0} :the time is {1}".format(os.getpid(),time.ctime()))
            time.sleep(self.interval)
            n -= 1


if __name__ == '__main__':
    p = ClockProcess(3)
    p2 = ClockProcess(2)
    p.start()
    p2.start()
    p.join()
    p2.join()
    print("over")