#多线程
from threading import Thread

#多线程写法1
# def func():
#     for i in range(1000):
#         print("func",i)
#
# if __name__ =='__main__':
#     t=Thread(target=func())
#     t.start()
#     for i in range(1000):
#         print("main",i)

#多线程写法2
# class MyThread(Thread):
#     def run(self):
#         for i in range(1000):
#             print("func",i)
#
# if __name__=="__main__":
#     t=MyThread()
#     t.start()
#     for i in range(1000):
#         print("main",i)
from concurrent.futures import ThreadPoolExecutor

def fn(name):
    for i in range(1000):
        print(name,i)

if __name__=='__main__':
    with ThreadPoolExecutor(10) as t:#造一个有10个线程的线程池
        for i in range(100):#100个任务
            t.submit(fn,name=f"线程{i}")