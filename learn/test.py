import time
from multiprocessing import Process


def run():
    i = 0
    while i < 3:
        i += 1
        time.sleep(1)
        print("113")

if __name__ == '__main__':
    p = Process(target=run)
    # p.daemon = True
    p.start()
    p.join()
    print(1)

# from multiprocessing import Process, Value, Array
# import time
# from multiprocessing import Pool
# import time
# import numpy as np
#
#
#
#
# def run(iteration):
#     # 模拟一个耗时的计算任务
#     result = 0
#     for i in range(iteration):
#         result += i
#     return result
#
#
# if __name__ == '__main__':
#     start_time = time.time()  # 记录开始时间
#
#     # 定义任务列表
#     iterations = [1000000, 1000000, 1000000, 1000000, 1000000]
#
#     # 创建一个进程池，使用所有可用的CPU核心
#     with Pool() as pool:
#         results = pool.map(run, iterations)  # 并行执行任务
#
#     end_time = time.time()  # 记录结束时间
#     elapsed_time = end_time - start_time  # 计算总时间
#
#     print(f"Elapsed time: {elapsed_time} seconds")
#     print(f"Results: {results}")
#     with counter.get_lock():
#         counter.value += 1
#     for i in range(len(array)):
#         array[i] += 1
#
#
# if __name__ == "__main__":
#     counter = Value('i', 0)  # 'i' indicates an integer
#     array = Array('d', [0.0, 1.1, 2.2])  # 'd' indicates a double precision float
#
#     processes = [Process(target=increment, args=(counter, array)) for _ in range(3)]
#
#     for p in processes:
#         p.start()
#     for p in processes:
#         p.join()
#
#     print(counter.value)  # Expected output: 3
#     print(array[:])  # Expected output: [3.0, 4.1, 5.2]
# # 进程间的通信可以使用Queue（）
# from multiprocessing import Process, Queue
#
# import time
# def producer(queue):
#     for i in range(5):
#         time.sleep(1)
#         queue.put({"name":"producer","status":1})
#         print(f"Produced: {i}")
#
#
# def consumer(queue):
#     while True:
#         # item = queue.get()
#         item = queue.get()  # 非阻塞获取
#         if item is None:
#             break
#         print(f"Consumed: {item.get('name')} finsh")
#
#
# if __name__ == "__main__":
#     queue = Queue()
#
#     producer_process = Process(target=producer, args=(queue,))
#     consumer_process = Process(target=consumer, args=(queue,))
#
#     # producer_process.start()
#     consumer_process.start()
#     producer_process.start()
#     # consumer_process.join()
