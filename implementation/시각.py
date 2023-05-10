def solution1():
    n = int(input())

    cur_hour = 0
    cur_min = 0
    cur_sec = 0

    ans = 0

    while cur_hour <= n:
        if "3" in str(cur_sec) or "3" in str(cur_min) or "3" in str(cur_hour):
            ans += 1

        cur_sec += 1

        if cur_sec == 60:
            cur_sec = 0
            cur_min += 1
        if cur_min == 60:
            cur_hour += 1
            cur_min = 0

    print(ans)


def solution2():
    h = int(input())

    count = 0
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                if "3" in str(i) + str(j) + str(k):
                    count += 1

    print(count)


# solution1()
solution2()
