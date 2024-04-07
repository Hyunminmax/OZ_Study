import psutil, os


print('메모리 사용량 조회')

memory_dict = dict(psutil.virtual_memory()._asdict())
print(memory_dict)

total = memory_dict['total']
available = memory_dict['available']
percent = memory_dict['percent']

print(f'메모리 총량: {total}')
print(f'메모리 즉시 제공 가능량: {available}')
print(f'메모리 사용률: {percent}')
