def rotatelist(l, k):
    if k <= 0:
        return l
    k = k % len(l)
    return l[k:] + l[:k]
print(rotatelist([1,2,3,4,5],12))