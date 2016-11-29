import requests
import gevent
import re

"""
1.线程和进程的操作是由程序触发系统接口，最后的执行者是系统;
2.对于多线程应用，CPU通过切片的方式来切换线程间的执行，线程切换时需要耗时（保存状态，下次继续）;
3.多线程用锁，很容易造成数据不稳定,无法使用发挥多核CPU的能力;多进程耗资源;

1.协程的操作则是程序员
2.只使用一个线程，在一个线程中规定某个代码块执行顺序
3.当程序中存在大量不需要CPU的操作时（IO），适用于协程
"""
# 第三方的gevent为Python提供了比较完善的协程支持
# 爬取豆瓣图书TOP250名字

def get_html(url):
    html = requests.get(url, verify=False).text
    book_list = re.findall(r'&#34; title="(.*?)"', html)
    print(book_list)


class MyGreenlet(gevent.Greenlet):
    def __init__(self, func):
        gevent.Greenlet.__init__(self)
        self.func = func

    def _run(self):
        # gevent.sleep(self.n)
        self.func


def main():
    base_url = "https://book.douban.com/top250?start="
    page_index = ["0", "25", "50"]
    count = len(page_index)
    green_let = []
    for i in page_index:
        page_url = base_url + i
        green_let.append(MyGreenlet(get_html(page_url)))
    for j in range(0, count):
        green_let[j].start()
    for k in range(0, count):
        green_let[k].join()


if __name__ == '__main__':
    main()
