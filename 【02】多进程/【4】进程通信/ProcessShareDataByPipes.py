from multiprocessing import Process, Pipe
import time

"""
Pipe方法返回(conn1, conn2)代表一个管道的两个端。
Pipe方法有duplex参数:
duplex 为 True(默认值)，那么这个管道是全双工模式，也就是说conn1和conn2均可收发。
duplex 为 False，conn1只负责接受消息，conn2只负责发送消息。
"""


def proc1(pipe):
    pipe.send('hello')
    print('proc1 rec:', pipe.recv())  # 如果接受不到就一直阻塞进程


def proc2(pipe):
    print('proc2 rec:', pipe.recv())
    time.sleep(5)
    pipe.send('hello, too')


# Build a pipe
pipe = Pipe()

# Pass an end of the pipe to process 1
p1 = Process(target=proc1, args=(pipe[0],))

# Pass the other end of the pipe to process 2
p2 = Process(target=proc2, args=(pipe[1],))

p1.start()
p2.start()
p1.join()
p2.join()
