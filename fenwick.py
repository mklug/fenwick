class FenwickTree:

    def __init__(self, size):
        # reindex
        self.tree = [None] + [0] * size

    def _lowest_one_bit(index):
        return index & -index

    @classmethod
    def treeify(cls, nums):
        N = len(nums)
        ft = cls(N)
        ft.tree = [None] + nums
        for index, value in enumerate(ft.tree[1:]):
            index += 1
            parentIndex = index + FenwickTree._lowest_one_bit(index)
            if parentIndex < N:
                ft.tree[parentIndex] += value
        return ft

    def prefixSum(self, index):
        if not 0 <= index < len(self.tree)-1:
            raise IndexError("Index out of range")
        index += 1  # reindex
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= FenwickTree._lowest_one_bit(index)
        return res

    def rangeSum(self, left_index, right_index):
        if not 0 <= left_index <= right_index < len(self.tree)-1:
            raise IndexError("Index out of range or order")
        if left_index == 0:
            return self.prefixSum(right_index)
        return self.prefixSum(right_index) - self.prefixSum(left_index-1)

    def getIndex(self, index):
        if not 0 <= index < len(self.tree)-1:
            raise IndexError("Index out of range")
        if index == 0:
            return self.tree[1]
        return self.rangeSum(index, index)

    def setIndex(self, index, value):
        if not 0 <= index < len(self.tree)-1:
            raise IndexError("Index out of range")
        delta = value - self.getIndex(index)
        index += 1  # reindex
        while index < len(self.tree):
            self.tree[index] += delta
            index += FenwickTree._lowest_one_bit(index)

    def __setitem__(self, index, value):
        self.setIndex(index, value)

    def __getitem__(self, index):
        return self.getIndex(index)

    def __len__(self):
        return len(self.tree) - 1
