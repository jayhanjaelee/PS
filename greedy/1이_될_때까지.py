n, k = map(int, input().split())

ans = 0

while True:
    if n == 1:
        break

    if n % k == 0:
        n /= k
    else:
        n -= 1

    ans += 1

print(ans)
