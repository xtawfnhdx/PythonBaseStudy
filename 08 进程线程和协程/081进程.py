import os
from multiprocessing import Process


def D1():
    pid = os.fork()
    if pid < 0:
        print('创建进程失败')
    if pid == 0:
        print('我是子进程（%s）,父进程id：（%s）' % (os.getpid(), os.getppid()))
    if pid > 0:
        print('我（%s）是父进程,创建了一个子进程(%s)' % (os.getpid(), pid))


def child_proc(name):
    print('Run Child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    # print('D1--------------------')
    # D1()
    print('D2--------------------')

    print('Parent process %s。' % os.getpid())
    # 用来创建一个进程对象
    p = Process(target=child_proc, args=('test',))
    print('Process will start')
    p.start()
    p.join()
    print('Process end.')
