from multiprocessing import Process, current_process

# 进程各自持有一份数据，默认无法共享数据
# 进程间无法共享内存数据
# 期望输出[0到10的随机排列的列表],实际上不可能实现




li = []


def foo(i):
    li.append(i)
    print('{} say hi'.format(current_process().name), li)


if __name__ == '__main__':

    for i in range(10):
        p = Process(target=foo, name="process {}".format(i), args=(i,))
        p.start()

    print('{} ending'.format(current_process().name), li)

"""
output:

process 0 say hi [0]
process 1 say hi [1]
process 2 say hi [2]
process 3 say hi [3]
process 4 say hi [4]
process 5 say hi [5]
process 6 say hi [6]
process 7 say hi [7]
MainProcess ending []
process 8 say hi [8]
process 9 say hi [9]
"""
