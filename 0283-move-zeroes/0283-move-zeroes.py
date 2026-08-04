class Solution(object):
    def moveZeroes(self, nums):
        nums.sort(key=lambda x: x == 0)