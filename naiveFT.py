class NaiveFT:

    def _prefixSums(nums):
        if len(nums) == 0:
            return []
        res = [nums[0]]
        for x in nums[1:]:
            res.append(res[-1] + x)
        return res

    def __init__(self, nums):
        self.nums = nums
        self.prefix_sums = NaiveFT._prefixSums(nums)

    def prefixSum(self, index):
        return self.prefix_sums[index]

    def rangeSum(self, left_index, right_index):
        if left_index == 0:
            return self.prefix_sums[right_index]
        return self.prefix_sums[right_index] - self.prefix_sums[left_index-1]

    def getIndex(self, index):
        return self.nums[index]

    def setIndex(self, index, value):
        self.nums[index] = value
        self.prefix_sums = NaiveFT._prefixSums(self.nums)

    def __setitem__(self, idx, value):
        self.nums[idx] = value
        self.prefix_sums = NaiveFT._prefixSums(self.nums)

    def __getitem__(self, index):
        return self.nums[index]

    def __len__(self):
        return len(self.nums)

    def __iter__(self):
        yield from self.nums
