foods = ['소고기', '양고기', '돼지고기']

print(id(foods))
print('논리메모리주소:', hex(id(foods)))

#b접두사(prefix)는 byte로 출력하겠다.
mv = memoryview(b"beef is very deilicious")
# mv = memoryview(b"소고기는 맛있어")

print(mv)
print(mv[0])
print(mv[1])
print(mv[2])
print(mv[3])