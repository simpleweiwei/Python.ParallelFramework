from multiprocessing import Process, Array

# 使用Array可以在进程间共享数据
"""
‘c’: ctypes.c_char　　　　 ‘u’: ctypes.c_wchar　　　　‘b’: ctypes.c_byte　　　　 ‘B’: ctypes.c_ubyte
‘h’: ctypes.c_short　　　  ‘H’: ctypes.c_ushort　　  ‘i’: ctypes.c_int　　　　　 ‘I’: ctypes.c_uint
‘l’: ctypes.c_long,　　　　‘L’: ctypes.c_ulong　　　　‘f’: ctypes.c_float　　　　‘d’: ctypes.c_double
"""


def f(a):
    for i in range(len(a)):
        a[i] = -a[i]


def twice(a):
    for i in range(len(a)):
        a[i] *= 2


if __name__ == '__main__':
    arr = Array('i', range(10))
    p = Process(target=f, args=(arr,))
    p2 = Process(target=twice, args=(arr,))
    p.start()
    p2.start()
    p.join()
    p2.join()
    print(arr[:])
