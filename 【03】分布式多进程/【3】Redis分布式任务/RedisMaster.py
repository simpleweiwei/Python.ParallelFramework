import multiprocessing
import random
import time

import redis

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
CHANNEL_DISPATCH = 'CHANNEL_DISPATCH'
CHANNEL_RESULT = 'CHANNEL_RESULT'


class MyMaster:
    def __init__(self):
        pass

    @staticmethod
    def start():
        MyServerResultHandleProcess().start()
        MyServerDispatchProcess().start()


class MyServerDispatchProcess(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)

    def run(self):
        r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        for i in range(1, 100):
            channel = CHANNEL_DISPATCH + '_' + str(random.randint(1, 3))
            print("Dispatch job %s to %s" % (str(i), channel))
            ret = r.publish(channel, str(i))
            if ret == 0:
                print("Dispatch job %s failed." % str(i))
            time.sleep(5)


class MyServerResultHandleProcess(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)

    def run(self):
        r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        p = r.pubsub()
        p.subscribe(CHANNEL_RESULT)
        for message in p.listen():
            if message['type'] != 'message':
                continue
            print("Received finished job %s" % message['data'])


if __name__ == "__main__":
    MyMaster.start()
    time.sleep(10000)
