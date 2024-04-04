from multiprocessing import Process
import os, time

def write():
    print(f'{os.getpid()}가 파일을 쓴다.')
    with open('13.txt', 'w') as f:
        f.write('hello')

def reader():
    print(f'{os.getpid()}가 파일을 쓴다.')
    with open('13.txt', 'r') as f:
        print(f.read())
    


if __name__ == '__main__':
    p1 = Process(target=write)
    p1.start()

    time.sleep(2)

    p2 = Process(target=reader)
    p2.start()    
