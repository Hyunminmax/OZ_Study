# 기본적인 파일 입출력 예제
import glob # 파일이름의 패턴을 이용해 한꺼번에 접근하기
import fileinput
import fnmatch, os

with open('number_one.txt', 'w') as f:
    f.write('11')

with open('number_two.txt', 'w') as f:
    f.write('22')

with open('number_three.txt', 'w') as f:
    f.write('33')

with open('number_four.txt', 'w') as f:
    f.write('44')

for filename in glob.glob('*.txt', recursive=True):
    print(filename)

with fileinput.input(glob.glob('*.txt')) as f:
    for line in f:
        print(line)

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, "??????_*.txt"):
        print(filename)