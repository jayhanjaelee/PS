n = int(input())
seats = input()
seats_info = []
seats_step = 0

for _ in range(len(seats)):
    try:
        s = seats[seats_step]
        if s == "S":
            seats_info.append("*")
            seats_info.append(s)
            seats_info.append("*")
            seats_step += 1
        elif s == "L":
            if seats_step + 1 > len(seats):
                break
            next_s = seats[seats_step + 1]
            seats_info.append("*")
            seats_info.append(s)
            seats_info.append(next_s)
            seats_info.append("*")
            seats_step += 2
    except IndexError as e:
        break

cup_cnt = "".join(seats_info).replace("**", "*").count("*")

print(n if cup_cnt > n else cup_cnt)