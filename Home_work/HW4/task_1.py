def union(a, b):
    c = a.union(b)
    return sorted(c, key=int)

numList1 = set(input().split())
numList2 = set(input().split())

print(*union(numList1, numList2))