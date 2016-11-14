from multiprocessing import Pool
import time


# 千万不要一创建进程就立马获取值，这样就变同步了，时间就会变得很长

def foo(i):
    time.sleep(2)
    return i + 100


def bar(arg):
    return arg


if __name__ == '__main__':
    res_list = []
    t_start = time.time()
    pool = Pool(5)

    for i in range(10):
        res = pool.apply_async(func=foo, args=(i,), callback=bar)
        res_list.append(res)

    pool.close()
    pool.join()
    for res in res_list:
        print("异步获取的数值：" + str(res.get()))  # 注意这里是异步读取数据
    t_end = time.time()
    t = t_end - t_start
    print("the program time is {}".format(t))
