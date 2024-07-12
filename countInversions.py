from fenwick import FenwickTree
# Assume perm is an array whose entries
# are a permutation of  0,1,2,....,n-1.

# An inversion is a pair of indices (i,j)
# with i < j and perm[i] > perm[j].


def countInversions(perm):

    N = len(perm)
    ft = FenwickTree(N)
    for i in range(N):
        ft[i] = 1

    d = {}
    for i, x in enumerate(perm):
        d[x] = i

    res = 0
    for i in range(N):
        ft[d[i]] = 0
        res += ft.prefixSum(d[i])

    return res
