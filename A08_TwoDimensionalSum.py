H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
q = int(input())
Q = [list(map(int, input().split())) for _ in range(q)]
TT = [[0] * (W + 1) for _ in range(H)] #横方向累積和
T =  [[0] * (W + 1) for _ in range(H)] #TTの縦方向累積和

for h in range(H):
    for w in range(W):
        TT[h][w] = TT[h][w-1] + X[h][w]

for h in range(1, H+1):
    for w in range(1, W+1):
        T[h][w] = TT[h - 1][w] + X[h][w]

print(T)