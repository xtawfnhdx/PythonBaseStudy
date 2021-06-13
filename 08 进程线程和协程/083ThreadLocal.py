from threading import Thread, current_thread


def echo(name):
    print('%s %s' % (current_thread().name, name))


def calc():
    print('thread is %s' % current_thread().name)
    localNum = 0
    for _ in range(10000):
        localNum += 1
    echo(localNum)
    print('thread %s end' % current_thread().name)


if __name__ == '__main__':
    print('----------- %s start' % current_thread().name)
    threads = []
    for i in range(5):
        threads.append(Thread(args=calc(), name=i))
        threads[i].start()
    for i in range(5):
        threads[i].join()
    print('--------- %s end' % current_thread().name)
