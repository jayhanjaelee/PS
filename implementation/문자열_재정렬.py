def solution():
    S = list(input())

    strings = []
    numbers = []

    while len(S):
        data = S.pop(0)
        _ascii = ord(data)

        if _ascii >= 65 and _ascii <= 90:
            # string
            strings.append(data)
        elif _ascii >= 48 and _ascii <= 57:
            # number
            numbers.append(data)

    sorted_strings = sorted(strings)
    converted_numbers = map(int, numbers)
    print(f"{(''.join(sorted_strings)) + str(sum(converted_numbers))}")


def solution2():
    data = input()
    result = []
    value = 0

    for x in data:
        if x.isalpha():
            result.append(x)
        else:
            value += int(x)

    result.sort()

    if value != 0:
        result.append(str(value))

    print("".join(result))


# solution()
solution2()
