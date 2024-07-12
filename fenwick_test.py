import random
from naiveFT import NaiveFT
from fenwick import FenwickTree

SIZE = 50

ft = FenwickTree(SIZE)
nft = NaiveFT([0]*SIZE)

operations = ['prefixSum', 'getIndex', 'setIndex']

for _ in range(10000):
    x = random.randint(-100, 100)
    op = random.choice(operations)
    index = random.randint(0, SIZE-1)

    op_ft = getattr(ft, op)
    op_nft = getattr(nft, op)

    if op in {'prefixSum', 'getIndex'}:
        assert op_ft(index) == op_nft(index)

    elif op == 'setIndex':
        op_ft(index, x)
        op_nft(index, x)

    left = random.randint(0, SIZE-1)
    right = random.randint(left, SIZE-1)
    assert ft.rangeSum(left, right) == nft.rangeSum(left, right)
