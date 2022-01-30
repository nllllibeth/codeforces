from heapq import heappop, heappush
def heapsort(a):
    heap = []
    for element in a:
        heappush(heap, element)
    sorted_a = []
    while heap:
        sorted_a.append(heappop(heap))
    return sorted_a

t = int(input())
min_level = 0
for i in range(t):
    n = int(input())
    level = [int(k) for k in input().split()]
    level = heapsort(level)
    print(n - level.count(level[0]))





