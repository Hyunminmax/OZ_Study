#인터럽트 예제
import time, signal

def handler(signum, frame):
    print('키보드 인터럽트 감지')
    print('신호번호: ', signum)
    print('스택 프레임:', frame)
    exit()

signal.signal(signal.SIGINT, handler)

while True:
    print('5초 간격')
    time.sleep(5)