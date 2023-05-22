def solution():
    cook_time = int(input())

    times = [300, 60, 10]
    counts = [0] * 3

    for i, t in enumerate(times):
        counts[i] = cook_time // t
        cook_time %= t

    print("-1" if cook_time != 0 else " ".join(map(str, counts)))


solution()