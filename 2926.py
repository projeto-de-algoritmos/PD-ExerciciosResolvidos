class BIT:
    def __init__(self, size):
        self.bit = [-float('inf')] * (size + 1)

    def pre_max(self, idx):
        idx += 1
        ans = -float('inf')
        while idx > 0:
            ans = max(ans, self.bit[idx])
            idx -= idx & -idx
        return ans

    def update(self, idx, val):
        idx += 1
        while idx < len(self.bit):
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & -idx

class Solution:
    def maxBalancedSubsequenceSum(self, nums):
        mapping = sorted([num - i for i, num in enumerate(nums)])
        mapping = list(dict.fromkeys(mapping))
        bit = BIT(len(nums))
        ans = -float('inf')

        for i in range(len(nums)):
            x = nums[i]
            j = bisect.bisect_left(mapping, x - i)
            cur = max(bit.pre_max(j) + x, x)
            ans = max(ans, cur)
            bit.update(j, cur)

        return ans
