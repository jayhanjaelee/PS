def solution():
    y, x = input()

    dx = [-2, 2, -1, 1]
    dy = [-1, 1, 2, -2]

    ans = 0

    for i in range(len(dx)):
        for j in range(len(dy)):
            if i < 2 and j > 1 or i > 1 and j < 2:
                continue

            nx = int(x) + dx[i]
            ny = ord(y) + dy[i]

            if nx < 1 or ny < 97 or nx > 8 or ny > 104:
                continue

            ans += 1

    print(ans)


def solution2():
    """
    column 을 a의 아스키코드 값을 뺀 값에 1을 더하여
    column 의 범위를 97 부터가 아닌 1로 시작하여 더 직관적으로 구현함.
    """

    input_data = input()
    row = int(input_data[1])
    column = int(ord(input_data[0])) - int(ord("a")) + 1

    # 방향 벡터를 리스트 한개로 구현
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    result = 0

    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]

        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
            result += 1

    print(result)


# solution()
solution2()
