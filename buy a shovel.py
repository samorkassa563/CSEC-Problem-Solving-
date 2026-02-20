k, r = map(int, input().split())
 
for i in range(1, 11):  # try buying 1 to 10 shovels
    total = i * k
    if total % 10 == 0 or total % 10 == r:
        print(i)
        break
