Y, W = map(int, input().split())
win = 7 - max(Y, W)
total = 6

a, b = win, total
while b:
    a, b = b, a % b
 
print(f"{win//a}/{total//a}")
