import math
def dominos(n, m):
    if n % 2 == 0:
        return math.floor((n * m) / 2)
    else:
        return math.floor((n * m) / 2)
n, m = map(int, input().split())
print(dominos(n, m))
