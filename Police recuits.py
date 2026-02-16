    n = int(input())
    p = list(map(int, input().split()))
    hired = 0
    free = 0
    for i in range(n):
        if p[i] != -1:
            hired += p[i]
        else:
           if hired == 0:
               free += 1
           elif hired != 0:
               hired -= 1
    print(free)
