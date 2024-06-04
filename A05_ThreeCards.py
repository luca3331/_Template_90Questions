import itertools
N, K = map(int, input().split())
ary = [x for x in range(1, N + 1)]
ans = 0
# print([x for x in itertools.combinations_with_replacement([y for y in range(1, N + 1)], 3) if sum(x) == K])
for i in ary:
    for j in ary:
        # for k in ary:
        #     if K == i + j + k:
        #         ans += 1
        if K - i - j >= 1 and K - i - j <= N:
            ans += 1
print(ans)