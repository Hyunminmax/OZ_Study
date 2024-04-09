# OS 파일 시스템 관련 함수
import os

pwd = r"H:\My Drive\InBox\000000OZ\OZ_Study\Study\OS"

#디렉터리 내부 리스트 업
filenames = os.listdir(pwd)
print(filenames)

# 디렉터리인지 아닌지 여부
print(os. path.isdir(filenames[0]))
print(os. path.isdir(pwd + r"\test"))

# 파일인지 아닌지 여부
print(os. path.isfile(filenames[0]))
print(os. path.isfile(pwd + r"\test"))

# 파일이름과 확장자 분리
filepath = os.path.join(pwd, filenames[0])
# filepath = pwd + "\\" + filenames[0]
print(filepath)
name, ext = os.path.splitext(filepath)
print(name)
print(ext)