# https://www.acmicpc.net/problem/10870


def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return solution(n - 1) + solution(n - 2)


n = int(input())
ans = solution(n)
print(ans)
