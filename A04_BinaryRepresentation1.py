N = int(input())
result = list()
while N > 0:
    elem = N % 2
    N = N // 2
    result.append(str(elem))
print(''.join(result[::-1]).zfill(10))