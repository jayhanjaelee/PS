# https://www.acmicpc.net/problem/2920


def solution():
    nums = list(map(int, input().split()))

    ans = []
    for i in range(len(nums)):
        try:
            ans.append(nums[i + 1] - nums[i])
        except IndexError:
            pass

    if ans.count(1) == 7:
        print("ascending")
    elif ans.count(-1) == 7:
        print("descending")
    else:
        print("mixed")

    return


def solution2():
    n = list(map(int, input().split()))
    print("ascending" if n == sorted(n) else "descending" if n == sorted(n, reverse=True) else "mixed")


# solution()
solution2()
