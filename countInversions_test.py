import random
from countInversions import countInversions


def naiveCountInversions(perm):
    N = len(perm)
    res = 0
    for i in range(N):
        for j in range(i, N):
            if perm[i] > perm[j]:
                res += 1
    return res


for _ in range(10000):
    N = random.randint(1, 100)
    perm = [i for i in range(N)]
    random.shuffle(perm)
    assert naiveCountInversions(perm) == countInversions(perm)
