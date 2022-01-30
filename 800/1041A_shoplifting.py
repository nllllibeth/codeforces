remaining = int(input())
a = [int(i) for i in input().split()]
a = sorted(a)
missing = 0
cnt = 0
for k in range(len(a) - 1):
    missing = a[k + 1] - a[k]
    if missing > 1:
        cnt += missing - 1
print(cnt)
