line = input()
t = int(line)

while t > 0:
    line = input()
    n = int(line)

    line = input()
    om = list(map(int, line.split()))

    line = input()
    addy = list(map(int, line.split()))

    om_streak, om_max, addy_streak, addy_max = 0, 0, 0, 0
    for i in range(n):
        if om[i] != 0:
            om_streak += 1
        else:
            om_max, om_streak = max(om_max, om_streak), 0
        if addy[i] != 0:
            addy_streak += 1
        else:
            addy_max, addy_streak = max(addy_max, addy_streak), 0

    om_max = max(om_max, om_streak)
    addy_max = max(addy_max, addy_streak)

    if om_max > addy_max:
        print("Om")
    elif addy_max > om_max:
        print("Addy")
    else:
        print("Draw")

    t -= 1
