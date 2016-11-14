from multiprocessing import Pool


# 多使用pool的map函数
def do_add(n1):
    return n1 ** 2


if __name__ == '__main__':  # 必须加，否则出错
    pool = Pool(5)
    result = pool.map(do_add, [1, 2, 3, 4, 5, 6])
    pool.close()
    pool.join()
    print(result)
