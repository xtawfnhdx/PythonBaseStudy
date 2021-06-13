from threading import current_thread, Thread

golbal_dict = {}


def echo():
    num = golbal_dict[current_thread()]
    print('输出：%s %s' % (current_thread().name, num))


def calc():
    print('child thread %s start' % current_thread().name)
    golbal_dict[current_thread()] = 0
    for _ in range(10000):
        golbal_dict[current_thread()] += 1
    echo()
    print('child thread %s end' % current_thread().ident)


if __name__ == '__main__':
    print('parent thread is %s' % current_thread().name)
    threads = []
    for i in range(5):
        threads.append(Thread(target=calc(), name="text" + str(i)))
        threads[i].start()
    for i in range(5):
        threads[i].join()
    print('parent thread is %s end' % current_thread().name)
