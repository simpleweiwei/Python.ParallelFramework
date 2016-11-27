import multiprocessing
import time

import redis

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
CHANNEL_DISPATCH = 'CHANNEL_DISPATCH'
CHANNEL_RESULT = 'CHANNEL_RESULT'


class MySlave:
    def __init__(self):
        pass

    @staticmethod
    def start():
        for i in range(1, 4):
            MyJobWorkerProcess(CHANNEL_DISPATCH + '_' + str(i)).start()


class MyJobWorkerProcess(multiprocessing.Process):
    def __init__(self, channel):
        multiprocessing.Process.__init__(self)
        self.channel = channel

    def run(self):
        r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        p = r.pubsub()
        p.subscribe(self.channel)
        for message in p.listen():
            if message['type'] != 'message':
                continue
            print("%s: Received dispatched job %s " % (self.channel, message['data']))
            print("%s: Run dispatched job %s " % (self.channel, message['data']))
            time.sleep(2)
            print("%s: Send finished job %s " % (self.channel, message['data']))
            ret = r.publish(CHANNEL_RESULT, message['data'])
            if ret == 0:
                print("%s: Send finished job %s failed." % (self.channel, message['data']))


if __name__ == "__main__":
    MySlave.start()
    time.sleep(10000)
