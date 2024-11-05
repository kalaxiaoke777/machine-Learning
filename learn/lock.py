from multiprocessing import Process, Lock, Value

def worker(lock, counter):
    # lock.acquire()  # 获取锁
    counter.value += 1
    print(f'Counter value is {counter.value}')


if __name__ == '__main__':
    lock = Lock()
    counter = Value('i', 0)  # 创建一个共享的整数变量，初始值为0
    processes = []

    for i in range(5):
        p = Process(target=worker, args=(lock, counter))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()