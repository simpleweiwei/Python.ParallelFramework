from multiprocessing import Pool, cpu_count
import time
import os


# 进程池可以方便的创建多个进程
# pool的大小默认是电脑的cpu核数，所以最好不要定太大
# Pool先调用close()方法才能join
def run(num):
    time.sleep(2)
    result = num * num
    print("process {}".format(os.getpid()) + "- result: " + str(result))


if __name__ == '__main__':
    test_list = [1, 3, 4, 7, 5, 9, 12]
    # 顺序执行，用的是同一个进程
    print("顺序执行")
    start_time = time.time()
    for i in test_list:
        run(i)
    end_time = time.time()
    time_span = int(end_time - start_time)
    print("串行用时:" + str(time_span))  # 14

    time.sleep(5)

    # 并行执行，用的是不同进程
    print("并行执行1")
    start_time2 = time.time()
    print("总cpu数：" + str(cpu_count()))
    p = Pool(5)  # 最多同时5个进程工作
    for j in test_list:
        p.apply_async(run, (j,))  # 注意此时参数类型
    p.close()
    p.join()
    end_time2 = time.time()
    time_span2 = int(end_time2 - start_time2)
    print("并行1用时:" + str(time_span2))  # 4

    print("并行执行2")
    start_time3 = time.time()
    p = Pool(5)
    p.map(run, test_list)  # 此处巧妙地使用了map函数
    p.close()
    p.join()
    end_time3 = time.time()
    time_span3 = int(end_time3 - start_time3)
    print("并行2用时:" + str(time_span3))  # 4
