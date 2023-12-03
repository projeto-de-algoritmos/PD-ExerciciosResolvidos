from typing import List

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        v = [0] * (n + 1)
        dp = [0] * (n + 1)
        sk = [(0, 0)]

        for i in range(1, n + 1):
            v[i] = v[i - 1] + nums[i - 1]

        for i in range(1, n + 1):
            low, high = 0, len(sk) - 1
            p = 0

            while low <= high:
                mid = low + (high - low) // 2

                if sk[mid][0] <= v[i]:
                    p = max(p, mid)
                    low = mid + 1
                else:
                    high = mid - 1

            index = sk[p][1]

            dp[i] = dp[index] + 1

            add = 2 * v[i] - v[index]

            while sk and sk[-1][0] >= add:
                sk.pop()

            sk.append((add, i))

        return dp[n]
