from itertools import combinations
arr = list(map(int, input().rstrip().split()))
def minad(arr):
    listy = []
    comb = combinations(arr, 2)
    comb = list(comb)
    for i in comb:
        v = abs(i[0]-i[1])
        listy.append(v)
    print(listy)

print(minad(arr))