'''
십진법의 이해: 10개의 기호를 이용해서 숫자를 표현하는 체계

이진법의 이해 : 2개의 기호를 이용해서

팔진법

십육진법

'''


number = 99

b_num = bin(number)
print(b_num)

o_num = oct(number)
print(o_num)

h_num = hex(number)
print(h_num)

b_num = bin(number)
print(b_num)

o_num = oct(int(b_num[2:], 2))
print(o_num)

h_num = hex(int(o_num[2:], 8))
print(h_num)