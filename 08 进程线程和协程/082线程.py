#thread 低级模块
#threading 高级模块，对thread进行封装
from threading import Thread, current_thread


def thread_test(name):
    print('thread %s is running...' % current_thread().name)
    print('hello ', name)
    print('thread %s ended.' % current_thread().name)


if __name__ == '__main__':
    print('thread %s is runnging...' % current_thread().name)
    print('hello world')
    t = Thread(target=thread_test, args=('test',), name='TestThread')
    t.start()
    t.join()
    print('thread %s ended' % current_thread().name)
