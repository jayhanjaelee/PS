from collections import deque

t = int(input())
# s = [1,1,1,1,1,9]
for _ in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    q = deque()
    for i, x in enumerate(s):
        q.append((i, x))
    s.sort()
    while q:
        i, x = q.popleft()
        print(i, x)
