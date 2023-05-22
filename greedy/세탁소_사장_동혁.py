t = int(input())

coin_types = [25, 10, 5, 1]

for _ in range(t):
    c = int(input())

    counts = [0] * 4

    for i, coin in enumerate(coin_types):
        counts[i] = c // coin
        c %= coin

        if c == 0:
            break

    print(" ".join(map(str, counts)))
