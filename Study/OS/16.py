from multiprocessing import Process, Value, Lock
import threading

def counter1(snum, cnt):
# def counter1(snum, cnt, lock):
    # lock.acquire()
    try:
        for i in range(cnt):
            snum.value += 1
    finally:
        print('끝')
    

def counter2(snum, cnt):
# def counter2(snum, cnt, lock):
    # lock.acquire()
    try:
        for i in range(cnt):
            snum.value -= 1
    finally:
        print('끝')

if __name__ == '__main__':
    lock = Lock()
    shared_number = Value('i', 0)
    t1 = threading.Thread(target=counter1, args=(shared_number, 15000))
    t1.start()
    
    t2 = threading.Thread(target=counter2, args=(shared_number, 15000))
    t2.start()
    
    t1.join()
    t2.join()                            

    print("finally, number is", shared_number.value)