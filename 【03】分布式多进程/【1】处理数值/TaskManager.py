# 导入managers子模块中的BaseManager类，这个类封装了一些常用的网络传输和接口方法
from multiprocessing.managers import BaseManager
import queue, time, random


"""
任务调度进程
"""


# 1.初始化两个queue消息列队，一个用于传输，一个用于接收
task_queue = queue.Queue()
result_queue = queue.Queue()


# 2.新建一个类，继承BaseManager的所有方法和属性
class QueueManager(BaseManager):
    pass


# 3.把创建的两个队列注册在网络上，利用register方法
# 生成两个接口函数，名为"get_task_queue"和"get_result_queue"（可以随便起名字），使用callable参数，将这两个接口函数关联到不同的queue对象上
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 4.监听本地的20016端口，验证码为"mymac"
manager = QueueManager(address=('', 20016), authkey=b'mymac')

# 5.启动网络监听
manager.start()
print("Address如下：")
print(manager.address)

# 6.获得经过封装之后的task和result队列
task, result = manager.get_task_queue(), manager.get_result_queue()

# 随机生成5个1~1000以内的数字，将它们放到进程中的queue网络接口消息列队中
for x in range(5):
    n = random.randint(1, 1000)
    print("将整数'%s'放入待发送的消息列队..." % n)
    task.put(n)

# 之后这个程序将被阻塞，在20016端口上等待消息的返回
print("等待计算结果返回...")
for x in range(5):
    r = result.get(True)
    print(r)

# 关闭接口，释放资源
manager.shutdown()
print("over")
