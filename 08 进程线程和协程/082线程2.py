from threading import Thread, current_thread, Lock

num = 0
lock = Lock()


def calc():
    print('child thread %s start' % current_thread().name)
    global num
    for _ in range(10000):
        # 获取锁
        lock.acquire()
        num += 1
        # 释放锁
        lock.release()
    print('child thread %s end' % current_thread().name)


if __name__ == '__main__':
    print('parent thread %s start' % current_thread().name)
    threads = []
    for i in range(5):
        threads.append(Thread(target=calc()))
        threads[i].start()
    for i in range(5):
        threads[i].join()
    print('global num:', num)
    print('parent thread %s end' % current_thread().name)
