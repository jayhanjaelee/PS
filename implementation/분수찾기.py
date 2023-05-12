def solution():
    X = int(input())

    row, col = 1, 1
    directions = [(0, 1), (1, -1), (1, 0), (-1, 1)]

    s = 0
    for i in range(X - 1):
        i %= 4

        d_row = directions[i][0]
        d_col = directions[i][1]

        if i == 1:
            s = 1

        if i == 3:
            s = 2

        row += d_row
        col += d_col

    print(f"{row}/{col}")

    return


solution()
