from multiprocessing import Process
import os, time

def water():
    while True:
        try:
            print('물 프로세스 아이디:', os.getpid())
            print('물 부모 프로세스 아이디:', os.getppid())
        except KeyboardInterrupt:
            break

def lemonWater():
    while True:
        try:
            print('레몬물 프로세스 아이디:', os.getpid())
            print('레몬물 부모 프로세스 아이디:', os.getppid())
        except KeyboardInterrupt:
            break

def hotWater():
    while True:
        try:
            print('뜨거운 물 프로세스 아이디:', os.getpid())
            print('뜨거운 물 부모 프로세스 아이디:', os.getppid())
        except KeyboardInterrupt:
            break   
    
if __name__ == "__main__":
    print('07.py 프로세스 아이디:', os.getpid())
    child1 = Process(target=water)
    child1.start()
    child2 = Process(target=lemonWater)
    child2.start()
    child3 = Process(target=hotWater)
    child3.start()
    