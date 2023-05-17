# https://www.acmicpc.net/problem/1316

N = int(input())
cnt = 0

while N:
    words = input()
    checker = [-1] * 26
    group_word = True

    for i in range(len(words)):
        if checker[ord(words[i]) - ord("a")] == -1:
            checker[ord(words[i]) - ord("a")] = True
        elif words[i] != words[i - 1]:
            group_word = False
            break

    if group_word:
        cnt += 1

    N -= 1

print(cnt)
