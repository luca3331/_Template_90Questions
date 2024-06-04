N, Q = map(int, input().split())
A = list(map(int, input().split()))
T = [0] * (N + 1)
for i in range(1, N+1):
    T[i] = A[i-1] + T[i-1]

LR = [map(int, input().split()) for _ in range(Q)]
for l, r in LR:
    print(T[r] - T[max(l-1, 0)])
