from multiprocessing import Process
import os

def func():
    print('안녕 난 함수야')
    print('내 프로세스 아이디:', os.getpid())
    print('내 부모 프로세스 아이디:', os.getppid())

if __name__ == "__main__":
    print('06.py 프로세스 아이디:', os.getpid())
    child1 = Process(target=func)
    child1.start()
    child2 = Process(target=func)
    child2.start()
    child3 = Process(target=func)
    child3.start()
    child4 = Process(target=func)
    child4.start()