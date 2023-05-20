n = int(input())

coin_types = [500, 100, 50, 10, 5, 1]
payback = 1000 - n

cnt = 0
for coin in coin_types:
    cnt += payback // coin
    payback %= coin

print(cnt)