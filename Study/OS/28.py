# 파일 복사 또는 이동


import os
import shutil


pwd = r"H:\My Drive\InBox\000000OZ\OZ_Study\Study\OS"
filenames = os.listdir(pwd)

for filename in filenames:
    if "Victoria" in filename:
        origin = os.path.join(pwd, filename)
        print(origin)
        # shutil.copy(origin, os.path.join(pwd, "VictoriaCopy.txt"))
        shutil.move(origin, os.path.join(pwd, "test"))
