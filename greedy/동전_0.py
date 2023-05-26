n, k = map(int, input().split())
cnt = 0
coin_types = []

for i in range(n):
    coin = int(input())
    coin_types.append(coin)

for coin in sorted(coin_types, reverse=True):
    if k // coin == 0:
        continue

    cnt += k // coin
    k %= coin

print(cnt)
