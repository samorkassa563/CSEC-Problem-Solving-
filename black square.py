    a1, a2, a3, a4 = map(int, input().split())
    n = str(input())
    d = {}
    calories = 0
    d[1] = a1
    d[2] = a2
    d[3] = a3
    d[4] = a4
    for sq in n:
        calories += d[int(sq)]
    print(calories)
