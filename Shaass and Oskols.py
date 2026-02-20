n = int(input())
l = list(map(int, input().split()))
m = int(input())
 
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1  # convert to 0-based index
 
    if x > 0:
        l[x-1] += y-1
    if x < n-1:
        l[x+1] += l[x] - y
 
    l[x] = 0
 
for birds in l:
    print(birds)
