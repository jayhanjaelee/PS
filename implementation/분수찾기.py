# https://www.acmicpc.net/problem/1193
def solution():
    n = int(input())

    index = 0
    sum = 0

    # 몇번째 그룹인지? (index)
    while True:
        index += 1
        sum = int(index * (index + 1) / 2)

        if n <= sum:
            break

    # 그룹내에서 몇번째 숫자인지?
    num = int(n - (index * (index - 1) / 2))

    # 홀수 행인지 짝수 행인지?
    if index % 2 == 0:
        print(f"{num}/{index - num + 1}")
    else:
        print(f"{index - num + 1}/{num}")

    return


solution()
