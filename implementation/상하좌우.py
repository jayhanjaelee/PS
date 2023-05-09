n = int(input())

directions = input().split()
# R U L D
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

direction_indices = {
    "R": 0,
    "U": 1,
    "L": 2,
    "D": 3,
}

x, y = 1, 1

for d in directions:
    i = direction_indices[d]

    # move
    if x + dx[i] < 1 or y + dy[i] < 1:
        continue

    x = x + dx[i]
    y = y + dy[i]

print(x, y)
