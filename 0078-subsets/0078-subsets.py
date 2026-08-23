class Solution(object):
    def subsets(self, nums):
        ans = [[]]
        for num in nums:
            ans += [x + [num] for x in ans]

        return ans
        