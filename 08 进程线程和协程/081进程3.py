from multiprocessing import Process, Queue
import time


def write_task(q):
    try:
        n = 1
        while n < 5:
            print('write,%d' % n)
            q.put(n)
            time.sleep(1)
            n += 1
    except BaseException:
        print('write_task error')
    finally:
        print('write_task end')


def read_task(q):
    try:
        n = 1
        while n < 5:
            print('read,%d' % q.get())
            time.sleep(1)
            n += 1
    except BaseException:
        print('read_task error')
    finally:
        print('read_task end')


# 验证进程间通讯
if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print('DONE')
