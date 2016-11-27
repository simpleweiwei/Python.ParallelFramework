# Python并发框架

Python下有许多开源的框架来支持分布式的并发：

* [PP](http://www.parallelpython.com/)

PP（Parallel Python）是一个轻量级的Python并行服务，主要是对多进程的封装

* [Celery](http://www.celeryproject.org/)

Celery是一个非常成熟的Python分布式框架，可以在分布式的系统中，异步的执行任务，并提供有效的管理和调度功能。参考[这里](http://my.oschina.net/taogang/blog/386077)

* [SCOOP](https://code.google.com/p/scoop/)

SCOOP （Scalable COncurrent Operations in Python）提供简单易用的分布式调用接口，使用Future接口来进行并发。

* [Dispy](https://github.com/pgiri/dispy)

相比起Celery和SCOOP，Dispy提供更为轻量级的分布式并行服务

* [Asyncoro](http://my.oschina.net/taogang/blog/386512)

Asyncoro是另一个利用Generator实现分布式并发的Python框架