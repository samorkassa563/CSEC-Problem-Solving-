n = int(input())
 
teams = []
for _ in range(n):
    home, guest = map(int, input().split())
    teams.append((home, guest))
 
count = 0
for i in range(n):      
    for j in range(n):  
        if i != j:
            if teams[i][0] == teams[j][1]:
                count += 1
 
print(count)
