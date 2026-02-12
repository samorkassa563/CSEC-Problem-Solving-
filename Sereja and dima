n = int(input())
cards = list(map(int, input().split()))
sereja, dima = 0, 0
turn = 0  # 0 = Sereja, 1 = Dima
left, right = 0, n - 1

while left <= right:
    if cards[left] > cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1

    if turn == 0:
        sereja += chosen
    else:
        dima += chosen
    turn = 1 - turn  # switch turnn

print(sereja, dima)
