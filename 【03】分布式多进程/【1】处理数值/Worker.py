from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass

# worker端只需要注册两个与调度端相同的网络接口函数名称即可
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 调度端IP
ip_address = "0.0.0.0"  # 此处是本机ip()
manager = QueueManager(address=(ip_address, 20016), authkey=b'mymac')  # 注意auth是字节对象

try:
    manager.connect()  # 连接
    task, result = manager.get_task_queue(), manager.get_result_queue()
    # 从调度端send_msg()接口get消息，然后将结果返回给调度端的receive_msg() 接口
    for x in range(5):
        print("开始从'%s'读取消息..." % ip_address)
        n = task.get(True)
        print("开始计算:%d*%d" % (n, n))
        r = "%d*%d=%d" % (n, n, n * n)
        result.put(r)
except Exception:
    print("连接失败。")
else:
    print("计算完成...")

