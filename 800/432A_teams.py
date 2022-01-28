n, k = map(int, str(input()).split())
team = [int(i) for i in input().split()]
possible_k = 5 - k
cnt = 0
for j in range(n):
    if team[j] <= possible_k:
        cnt += 1
print(cnt // 3)