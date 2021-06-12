import os
import time
from multiprocessing import Pool


def foo(x):
    print('Run task %s (pid:%s)' % (x, os.getpid()))
    time.sleep(5)
    print('Task %s result is :%s' % (x, x * x))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 最多能创建4个进程的进程池
    p = Pool(4)
    for i in range(5):
        # apply_async：异步执行任务
        p.apply_async(foo, args=(i,))
    print('Waiting for all subprocesses done...')
    # close关闭进程池，确保没有新的进程加入
    p.close()
    # join等待所有子进程执行完成
    p.join()
    print('All subprocesses done.')
