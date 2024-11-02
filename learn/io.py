#导入线程进程标准模块 
import multiprocessing as mp
import threading as td

#定义一个被线程和进程调用的函数 
def job(a,d):
    print(a,d)



if __name__ == '__main__':
    #创建线程和进程，只是定义线程或进程要做什么，传入的参数有什么，名字叫什么，但是还未开始工作。
    t1 = td.Thread(target=job,args=(1,2))
    p1 = mp.Process(target=job,args=(3,2))

    #分别启动线程和进程，线程与进程开始工作
    p1.start()
    p1.join()
    t1.start()



    #分别连接线程和进程，线程和进程join作用一致
    # t1.join()
    # p1.join()
