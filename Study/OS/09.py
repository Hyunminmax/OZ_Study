import threading, os

def func():
    print('물 프로세스 아이디:', os.getpid())
    print('물 스레드 아이디:', threading.get_native_id())

if __name__ == "__main__":
    print('기존 프로세스 아이디:', os.getpid())
    thread1 = threading.Thread(target=func)
    thread1.start()
