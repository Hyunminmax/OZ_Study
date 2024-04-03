from multiprocessing import Process
import os

def func():
    print('안녕 난 함수야')
    print('내 프로세스 아이디:', os.getpid())
    print('내 부모 프로세스 아이디:', os.getppid())

if __name__ == "__main__":
    print('05.py 프로세스 아이디:', os.getpid())
    child = Process(target=func).start()