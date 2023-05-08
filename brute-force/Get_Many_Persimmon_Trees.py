import sys

lines = [line.strip() for line in sys.stdin]
case_step = 0


def solve():
    # parsing
    global case_step

    tree_num = int(lines[case_step])

    if tree_num == 0:
        return

    field_width, field_height = list(map(int, lines[case_step + 1].split()))

    tree_start_index = case_step + 2
    tree_end_index = tree_start_index + tree_num

    tree = lines[tree_start_index:tree_end_index]
    tree = [[int(num) for num in t.split()] for t in tree]

    s, t = [int(x) for x in lines[tree_end_index].split()]

    origin_x, origin_y = 1, 1

    ans = 0
    while True:
        estate_width = (origin_x + s) - 1
        estate_height = (origin_y + t) - 1

        if estate_width > field_width:
            break

        # find tree
        tree_cnt = 0
        for [x, y] in tree:
            if x >= origin_x and x <= estate_width:
                if y >= origin_y and y <= estate_height:
                    tree_cnt += 1

        if tree_cnt > ans:
            ans = tree_cnt

        if estate_height > field_height:
            origin_y = 1
            origin_x += 1
        else:
            origin_y += 1

    print(ans)

    case_step = tree_end_index + 1
    solve()


solve()
